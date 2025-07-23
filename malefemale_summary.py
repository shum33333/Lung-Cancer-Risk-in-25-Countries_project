# 載入套件
import pandas as pd
import os

# 步驟一：讀取資料
file_path = "lung_cancer_prediction_dataset_Diagnosis_yes.csv"  # 請根據實際路徑調整
df = pd.read_csv(file_path)

# 步驟二：擷取性別與年齡欄位，並移除缺失值
df_age_gender = df[['Gender', 'Age']].dropna()

# 步驟三：依性別分組並計算年齡的描述性統計
summary_by_gender = df_age_gender.groupby('Gender')['Age'].describe().T

# 顯示統計結果
print("依性別對年齡的描述性統計：")
print(summary_by_gender)

# 步驟四：匯出成 Excel 檔（可選）
output_path = "年齡_按性別描述統計.xlsx"
summary_by_gender.to_excel(output_path)
print(f"\n結果已匯出為 Excel 檔案：{output_path}")
