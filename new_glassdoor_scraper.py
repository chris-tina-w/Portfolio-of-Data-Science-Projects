from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    # Initializing the webdriver
    options = webdriver.ChromeOptions()
    service = Service(path)
    
    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')
    
    # Initialize the driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1120, 1000)
    
    url = f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={keyword}&locT=&locId="
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:
        time.sleep(slp_time)

        # Test for the "Sign Up" prompt and get rid of it
        try:
            driver.find_element(By.CLASS_NAME, 'CloseButton').click()
        except (NoSuchElementException, TimeoutException):
            pass
        
        # Going through each job in this page
        job_buttons = driver.find_elements(By.CLASS_NAME, "JobsList_jobListItem__wjTHv")  # 'jl' for Job Listing. These are the buttons we're going to click.       
        for job_button in job_buttons:
            
            try:
                driver.find_element(By.CLASS_NAME, 'CloseButton').click()
            except (NoSuchElementException, TimeoutException):
                pass
            
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    company_name = driver.find_element(By.XPATH, './/h4[@class="heading_Heading__BqX5J heading_Subhead__Ip1aW"]').text
                    location = driver.find_element(By.XPATH, './/div[@class="JobDetails_location__mSg5h"]').text
                    job_title = driver.find_element(By.XPATH, './/h1[@class="heading_Heading__BqX5J heading_Level1__soLZs"]').text
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element(By.XPATH, './/div[@class="SalaryEstimate_medianEstimate__fOYN1"]').text
            except NoSuchElementException:
                salary_estimate = -1  # You need to set a "not found value. It's important."
            


            # Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            # Looking at company details
            try:
                details = driver.find_elements(By.XPATH, './/div[@class="JobDetails_overviewItem__cAsry"]')
                
                
                for detail in details:
                    label = detail.find_element(By.CLASS_NAME, 'JobDetails_overviewItemLabel__KjFln').text
                    value = detail.find_element(By.CLASS_NAME, 'JobDetails_overviewItemValue__xn8EF').text
                    if label == "Size":
                        size = value   
                    elif label == "Founded":
                        founded = value
                    elif label == "Type":
                        type_of_ownership = value
                    elif label == "Industry":
                        industry = value
                    elif label == "Sector":
                        sector = value
                    elif label == "Revenue":
                        revenue = value

            except NoSuchElementException:  # Rarely, some job postings do not have the "Company" tab.
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1


            if verbose:
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
                         "Salary Estimate" : salary_estimate,
                         "Company Name" : company_name,
                         "Location" : location,
                         "Size" : size,
                         "Founded" : founded,
                         "Type of ownership" : type_of_ownership,
                         "Industry" : industry,
                         "Sector" : sector,
                         "Revenue" : revenue,})
            
        try:
            driver.find_element(By.XPATH, './/li[@class="next"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)

# Usage example
path = "C:/Users/chris/Documents/ds_salary_proj/chromedriver.exe"
df = get_jobs('data scientist', 10, True, path, 10)
print(df)
