import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#df=pd.read_csv('/kaggle/input/lung-cancer-risk-in-25-countries/lung_cancer_prediction_dataset.csv')

df=pd.read_csv('D:/芳珊/202504_Python人工智慧與數據分析/Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv')

df.head()
print(df.head())

df.info()

#Number of cancer patients based on different countries

cancer_by_country = df[df['Lung_Cancer_Diagnosis'] == 'Yes']['Country'].value_counts()

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x=cancer_by_country.index, y=cancer_by_country.values, palette="coolwarm")
plt.xticks(rotation=90)
plt.xlabel("Country")
plt.ylabel("Number of Cancer Cases")
plt.title("Lung Cancer Cases by Country")
plt.show()

#Age Factor for Having Cancer 
plt.figure(figsize=(10, 5))
sns.histplot(df[df["Lung_Cancer_Diagnosis"] == "Yes"]["Age"], bins=30, kde=True, color="red", label="Cancer Patients")
# sns.histplot(df[df["Lung_Cancer_Diagnosis"] == "No"]["Age"], bins=30, kde=True, color="blue", label="Non-Cancer Patients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution of Cancer Patients")
# plt.legend()
plt.show()

#Cigarettes Per Day for People with and without Cancer
plt.figure(figsize=(8, 5))
sns.boxplot(x="Lung_Cancer_Diagnosis", y="Cigarettes_per_Day", data=df, palette="pastel")
plt.xlabel("Lung Cancer Diagnosis")
plt.ylabel("Cigarettes per Day")
plt.title("Cigarettes Per Day for Cancer vs Non-Cancer Patients")
plt.show()

