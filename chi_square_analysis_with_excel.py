
# 匯入套件
import pandas as pd
from scipy.stats import chi2_contingency

# 讀取資料集
df = pd.read_csv('lung_cancer_prediction_dataset.csv')

# 指定要分析的變項
factors = [
    'Smoker',
    'Passive_Smoker',
    'Family_History',
    'Air_Pollution_Exposure',
    'Occupational_Exposure',
    'Indoor_Pollution'
]
target = 'Lung_Cancer_Diagnosis'

# 建立結果儲存清單
results = []

# 逐一對每個變項執行卡方檢定
for factor in factors:
    # 建立列聯表
    table = pd.crosstab(df[factor], df[target])

    # 執行卡方檢定
    chi2, p, dof, expected = chi2_contingency(table)

    # 將結果加入清單
    results.append({
        '變項': factor,
        '卡方統計量': round(chi2, 2),
        '自由度': dof,
        'p值': round(p, 4),
        '顯著與否(p<0.05)': '顯著' if p < 0.05 else '不顯著'
    })

# 整理為 DataFrame 並輸出 Excel
results_df = pd.DataFrame(results)
results_df.to_excel('chi_square_analysis_result.xlsx', index=False)
print("卡方檢定結果已儲存為 chi_square_analysis_result.xlsx")
