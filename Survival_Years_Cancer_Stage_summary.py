# 載入必要套件
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#步驟一：讀取 CSV 檔案
file_path = "lung_cancer_prediction_dataset_Diagnosis_yes.csv"  # 修改為你的路徑
df = pd.read_csv(file_path)

# 步驟二：選擇需要的欄位並清理缺失值
df_stage_survival = df[['Cancer_Stage', 'Survival_Years']].dropna()

# 步驟三：過濾只包含 Stage 1~4 的資料
valid_stages = ['Stage 1', 'Stage 2', 'Stage 3', 'Stage 4']
df_stage_survival = df_stage_survival[df_stage_survival['Cancer_Stage'].isin(valid_stages)]

# 步驟四：分組描述性統計分析
summary_by_stage = df_stage_survival.groupby('Cancer_Stage')['Survival_Years'].describe().T

# 步驟五：輸出結果至 console
print("存活年數描述性統計（依癌症期別）：")
print(summary_by_stage)

# 步驟六：匯出 Excel 檔案（可選）
output_path = "存活年數_癌症期別_描述統計.xlsx"
summary_by_stage.to_excel(output_path)
print(f"\n 結果已匯出至 Excel：{output_path}")
