import pandas as pd

# 匯入資料
df = pd.read_csv("lung_cancer_prediction_dataset.csv")


# 指定要分析的欄位
categorical_columns = [
    "Gender", "Smoker", "Passive_Smoker", "Family_History", "Lung_Cancer_Diagnosis",
    "Developed_or_Developing", "Healthcare_Access", "Early_Detection"
]

# 結果儲存清單
summary = []

# 逐欄計算分類統計
for col in categorical_columns:
    value_counts = df[col].value_counts(dropna=False)
    total = value_counts.sum()
    top_category = value_counts.idxmax()
    top_percent = round(value_counts.max() / total * 100, 1)
    categories = " / ".join(value_counts.index.astype(str).tolist())

    summary.append({
        "欄位名稱": col,
        "分類": categories,
        "最大占比": f"{top_category} ({top_percent}%)"
    })

# 輸出為表格
summary_df = pd.DataFrame(summary)
summary_df.to_excel("lung_cancer_prediction_dataset_類別變項統計摘要.xlsx", index=False)

print(" 統計完成並匯出 Excel 檔案 ")
