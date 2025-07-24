import matplotlib
matplotlib.use('TkAgg')  # 使用互動式圖形後端，確保圖表能彈出

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取資料
df = pd.read_csv('D:/shan/power-bi_advanced-courses/Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv')

print(df.head())
df.info()

# ----------------------------------------------------
# 圖 1：各國肺癌確診人數（長條圖）
# ----------------------------------------------------
cancer_by_country = df[df['Lung_Cancer_Diagnosis'] == 'Yes']['Country'].value_counts().reset_index()
cancer_by_country.columns = ['Country', 'Cancer_Cases']

plt.figure(figsize=(12, 6))
sns.barplot(data=cancer_by_country, x='Country', y='Cancer_Cases', hue='Country', palette='coolwarm', legend=False)
plt.xticks(rotation=90)
plt.xlabel("Country")
plt.ylabel("Number of Cancer Cases")
plt.title("Lung Cancer Cases by Country")
plt.tight_layout()
plt.savefig("01_Lung_Cancer_Cases_by_Country.png", dpi=300)
print(" 圖 1 已儲存：01_Lung_Cancer_Cases_by_Country.png")
plt.show()

# ----------------------------------------------------
# 圖 2：肺癌患者年齡分布（直方圖）
# ----------------------------------------------------
plt.figure(figsize=(10, 5))
sns.histplot(df[df["Lung_Cancer_Diagnosis"] == "Yes"]["Age"], bins=30, kde=True, color="red")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution of Cancer Patients")
plt.tight_layout()
plt.savefig("02_Age_Distribution_Cancer_Patients.png", dpi=300)
print(" 圖 2 已儲存：02_Age_Distribution_Cancer_Patients.png")
plt.show()

# ----------------------------------------------------
# 圖 3：不同診斷者每日吸菸量（盒鬚圖）
# ----------------------------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x="Lung_Cancer_Diagnosis", y="Cigarettes_per_Day", data=df, palette="pastel")
plt.xlabel("Lung Cancer Diagnosis")
plt.ylabel("Cigarettes per Day")
plt.title("Cigarettes Per Day for Cancer vs Non-Cancer Patients")
plt.tight_layout()
plt.savefig("03_Cigarettes_Per_Day_Boxplot.png", dpi=300)
print(" 圖 3 已儲存：03_Cigarettes_Per_Day_Boxplot.png")
plt.show()

# ----------------------------------------------------
# 圖 4：吸菸年數與肺癌診斷（盒鬚圖）
# ----------------------------------------------------
plt.figure(figsize=(7, 5))
sns.boxplot(x="Lung_Cancer_Diagnosis", y="Years_of_Smoking", data=df, palette="muted")
plt.xlabel("Lung Cancer Diagnosis")
plt.ylabel("Years of Smoking")
plt.title("Years of Smoking for Cancer vs Non-Cancer Patients")
plt.tight_layout()
plt.savefig("04_Years_of_Smoking_Boxplot.png", dpi=300)
print(" 圖 4 已儲存：04_Years_of_Smoking_Boxplot.png")
plt.show()
