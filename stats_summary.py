import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# 匯入資料
data = pd.read_csv("lung_cancer_prediction_dataset.csv")
df = data.copy()
print(df.head())

# 匯出用函式：將任何 DataFrame 輸出為 Excel
def export_to_excel(df, output_path="D:/shan/power-bi_advanced-courses/Lung-Cancer-Risk-in-25-Countries_project/基本統計摘要.xlsx", sheet_name="Summary", index=True):
    try:
        folder = os.path.dirname(output_path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        df.to_excel(output_path, sheet_name=sheet_name, index=index)
        print(f"\n 檔案已成功匯出至：{output_path}")
    except Exception as e:
        print(" 匯出失敗，錯誤如下：", e)

# 探索性資料分析
def basic_data_insights(df):
    """ 提供基本資料統計與匯出 summary 為 Excel。"""
    print("\n 資料維度（行數, 列數）: ", df.shape)
    print("\n 欄位名稱列表: \n", df.columns.to_list())
    print("\n 資料型別與缺值狀況:")
    print(df.info())
    print("\n 各欄位缺失值比例 (%):\n", (df.isna().sum()/len(df))*100)
    print("\n 重複紀錄數量: ", df.duplicated().sum())

    stats_summary = df.describe()
    print("\n 基本統計摘要:\n", stats_summary)

    # 匯出為 Excel
    export_to_excel(stats_summary, output_path="D:/shan/power-bi_advanced-courses/Lung-Cancer-Risk-in-25-Countries_project/基本統計摘要.xlsx", sheet_name="Summary", index=True)

# ▶呼叫分析
basic_data_insights(df)
