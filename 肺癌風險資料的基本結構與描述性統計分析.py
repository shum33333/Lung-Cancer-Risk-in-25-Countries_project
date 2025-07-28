import os
import math
import numpy as np
import pandas as pd

#df=pd.read_csv('D:/芳珊/202504_Python人工智慧與數據分析/Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv')
#df=pd.read_csv('D:/shan/power-bi_advanced-courses/Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv')
df = pd.read_csv("lung_cancer_prediction_dataset.csv")

df.head()
print(df.head())
#資料表的基本結構資訊
df.info()
#查看欄位名稱
df.columns
#描述性統計摘要，顯示所有「數值型欄位」的統計資訊
df.describe()
print(df.describe())