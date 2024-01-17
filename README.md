# Overview
Machine Learning robot I am building using python. I am going to analyze how student's test scores are affected based off of their Gender, Ethnicity, Parental level of education, Lunch, and Test preperation course. The dataset I will be pulling from is from [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977) and consists of 8 columns and 1000 rows.

# Life cycle of a Machine Learning Project
* Understanding the problem
* [Data Collection](notebook/data/stud.csv)
* Data Checks 
* [Exploratory Data Analysis](<notebook/Exploratory Data Analysis.ipynb>)
* Data Pre-Processing ([data_ingestion](src/components/data_ingestion.py),[data_transformation](src/components/data_transformation.py))
* [Model Training](src/components/model_trainer.py)
* Evaluate model
* [Push Model](app.py)

# Imported Data and Required Packages
#### Basic Import
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
```
#### Modelling
```
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
import warnings
from xgboost import XGBRegressor
```

# Installation
To install and run my code, follow these steps in terminal:
1. Clone the Repository:
```
git clone https://github.com/anthonyjcthomas/Student-Performance-Indicator.git
```
2. Navigate to Repository Directory:
```
cd Student-Performance-Indicator
```
3. Install Required Dependencies:
```
pip install -r requirements.txt
```

# Usage
To use the Student Performance Indicator, follow these steps:
1. Run the application:
```
python application.py
```
2. Open your web browser and go to:
```
http://127.0.0.1:5000/predictdata
```
3. On the webpage, you will need to fill out the following information:
* Gender
* Race/Ethnicity
* Parental Level of Education
* Type of Lunch
* Test Preparation Course
* Writing Score
* Reading Score
# License
This repository is licensed under the MIT License - see the [License.md](License.md) file for details.

# Contact
For any inquiries or further information, please contact Anthony Thomas
* Email: anthonyjcthomas@gmail.com
* Phone: 608-698-6333


