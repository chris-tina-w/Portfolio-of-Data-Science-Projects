# *Christina's Data Science Portfolio*
Welcome to my repository of data science projects! With a background in medicine, I am exploring the world of data science through academic study and self-directed learning. 

This collection highlights my journey of building technical skills and applying them to interesting real-world datasets and challenges. My goal is to bridge the gap between data and meaningful insights through machine learning and AI.

# Project 1: SQL and Tableau
In this project, I analysed a dataset featuring famous artists and their works using SQL and Tableau which showed that:
- Significant collections are concentrated in a few countries
- Few artists have reached an international audience, with many of their works confined to private collections
- Shifts in artistic preference influence what is displayed in museums and what holds value in the art market

### **Methodology**
- Designed an [**ER Diagram**](Famous%20Paintings/Art%20ER%20Diagram.jpg) to model the database structure.
- Performed [**Data Preprocessing**](Famous%20Paintings/art_preprocessing.ipynb) using Python and MySQL connector, including removing duplicates, changing data types, and creating primary and foreign keys.
- Executed [**SQL Queries**](Famous%20Paintings/art%20sql.ipynb) with MySQL.
- Developed an interactive [**Tableau Dashboard**](https://public.tableau.com/views/FamousArtistsandtheirWorks/Art?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) to visualise the queries. (Screenshots of the dashboards can be found [here](Famous%20Paintings/Dashboards/art%20dashboards.md))

### **ToolKit**
- Python, MySQL, MySQL.Connector, Pandas, Tableau

_Dataset from: https://data.world/atlas-query/paintings_

![](Famous%20Paintings/Dashboards/Story%201.png)

# Project 2: Regression with Python
In this project, I explored whether infrared thermography readings could effectively predict elevated body temperatures using regression analysis. 
- My [Body Temperature Regression Model](Infrared%20Thermography%20Regression/Infrared%20Thermography%20Regression.ipynb) was able to predict body temperatures with an error of 0.2404 degrees. 

### **Methodology**
- Applied Box-Cox transformation to normalise the target variable.
- Computed correlation matrix to assess relationships between predictors and target variable.
- Developed a data preprocessing pipeline, including imputation, ordinal encoding, and one-hot encoding.
- Set up a function to train and evaluate models with metrics including root mean squared error, coefficient of determination, and bias
- Trained data on linear regression, ridge regression, lasso regression, elasticnet regression, LGBMRegressor, and random forest regressor
- Implemented hyperparameter tuning for LGBMRegressor

### **ToolKit**
- Python, Numpy, Pandas, Matplotlib, Seaborn, SciPy, Scikit-learn

![](Infrared%20Thermography%20Regression/rmse_plot.jpg)

# Project 3: Unsupervised Machine Learning with K-Means Clustering
In this [Skin Lesion Image Compression Project](Skin%20Lesion%20K-Means%20Clustering/Skin%20Lesion%20K-Means%20Clustering.ipynb), I built a K-means clustering model from scratch to compress a medical image into 30 representative centroid colours. 
- Compressing medical imaging can enhance machine learning models by emphasising dominant patterns while reducing memory usage.

### **Methodology**
- Initialised random centroids.
- Assigned each data point to the nearest centroid.
- Computed the means of all points assigned to each centroid to update centroid positions.
- Repeated the process with K-means algorithm

### **ToolKit**
- Python, Numpy, Matplotlib
  
![](Skin%20Lesion%20K-Means%20Clustering/lesion_plot.jpg)

## More SQL Projects
  - [Gym Membership Queries with Oracle](Gym_SQL.ipynb): creating SQL queries, stored procedures, stored functions, and triggers
      
## More Machine Learning Projects
  - **Supervised Machine Learning**
    - **Regression**
      - [Coffee Bean Time Series Regression with Python](Coffee%20Bean%20Regression/Coffee%20Bean%20Regression.ipynb): Predicting coffee bean trading volume based on market price indicators using regression analysis 
    - **Classification**
      - [Edible Mushroom Classification with Python](Mushroom%20Classification/Mushroom%20Classification.ipynb): Implementing a decision tree algorithm from scratch to classify mushrooms into edible and poisonous categories
      - [Divorce Prediction with Weka](Divorce%20Prediction.ipynb): Conducting data mining analysis for divorce prediction using Weka
  - **Unsupervised Machine Learning**
    - **Anomaly Detection**
      - [Fraud Detection with Python](Transaction%20Fraud%20Anomaly%20Detection/Transaction%20Fraud%20Anomaly%20Detection.ipynb): Developing an anomaly detection algorithm from scratch to identify potential fraudulent activities
 
## More Data Analysis and Visualisation
  - [Cinema Analysis with R](Data%20Analysis%20of%20IMDB%20Dataset.ipynb): Analysing and visualising relationships between movie attributes using IMDb data
  - [Student Performance Analysis with R](Student%20Marks/Data%20Analysis%20of%20Student%20Marks.ipynb): Conducting a brief analysis and visualistion of student performance
  - [Dominance Matrices with R](Dominance%20Matrices.ipynb): Analysing AFL team rankings with dominance matrices in R
  

## My Study Approach
**Academic**
- Master of Data Science (La Trobe University)
- Graduate Certificate in Applied Data Science (Charles Sturt University) - Executive Dean's Award

**Online Courses**
- Coursera's Machine Learning Specialization with Andrew Ng
- Coursera's Deep Learning Specialization with Andrew Ng

**Textbooks**
- Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 2nd Edition by Aurélien Géron
- Modern Time Series Forecasting with Python by Manu Joseph
- Deep Learning with Python by François Chollet
- Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications by Chip Huyen
