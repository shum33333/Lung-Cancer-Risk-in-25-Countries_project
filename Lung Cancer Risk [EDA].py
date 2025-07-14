import os
import math
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))




# Load dataset and remove the first column

#df = pd.read_csv('/kaggle/input/lung-cancer-risk-in-25-countries/lung_cancer_prediction_dataset.csv').iloc[:, 1:]

#df=pd.read_csv('D:/芳珊/202504_Python人工智慧與數據分析/Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv')
df=pd.read_csv('D:\shan\power-bi_advanced-courses\Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv')
df.head()
print(df.head())

df.info()



df.columns

print(df.info())

df.describe()
print(df.describe())