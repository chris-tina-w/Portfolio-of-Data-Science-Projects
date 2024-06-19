### Machine Learning with Logistic Regression

Second in the ML micro-project series, in this project we will work with a fake advertising data set, indicating whether or not a particular internet user clicked on an advertisement.

We will create a logistic regression model that will predict whether or not a user will click on an ad, based on his/her features. As this is a binary classification problem, a logistic regression model is well suited here.


```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

ad_data = pd.read_csv('../data/advertising.csv')

ad_data.head()
