import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#Load Data
#data =  pd.read_csv("/kaggle/input/lung-cancer-risk-in-25-countries/lung_cancer_prediction_dataset.csv")
#data =  pd.read_csv("D:/芳珊/202504_Python人工智慧與數據分析/Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv")
data =  pd.read_csv('D:\shan\power-bi_advanced-courses\Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv')
df = data.copy()
df.head()
print(df.head())


#Exploratory Data Analysis
def basic_data_insights(df):
    """ This method provides basic details about data."""
    print("\n Dimension of data: ", df.shape)
    print("\n Columns of data: \n", df.columns.to_list())
    print( df.info())
    print("\n Percentage of null values in each column: \n",
         (df.isna().sum()/len(df))*100)
    print("\n Total duplicate records: ", df.duplicated().sum())
    print("\n Basic Statistical summary: ", df.describe())


# calling methoda
basic_data_insights(df)
