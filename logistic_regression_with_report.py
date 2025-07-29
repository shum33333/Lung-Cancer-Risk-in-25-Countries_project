import pandas as pd
import statsmodels.api as sm
import numpy as np

# 1. 讀取資料
df = pd.read_csv("lung_cancer_data_ConvertNum.csv", encoding="big5")

# 2. 將目標變數轉為 0/1（如果尚未處理，可取消註解下一行）
# df['Lung_Cancer_Diagnosis'] = df['Lung_Cancer_Diagnosis'].map({'Yes': 1, 'No': 0})

df['Cancer'] = df['Lung_Cancer_Diagnosis']

# 3. 選擇解釋變數
X = df[['Age', 'Smoker', 'Passive_Smoker', 'Family_History',
        'Air_Pollution_Exposure', 'Occupational_Exposure',
        'Indoor_Pollution', 'Healthcare_Access', 'Early_Detection']]

y = df['Cancer']

# 4. 加入截距項
X = sm.add_constant(X)

# 5. 建立與擬合模型
model = sm.Logit(y, X)
result = model.fit()

# 6. 顯示模型摘要
print(result.summary())

# 7. 額外：計算勝算比（Odds Ratio）
odds_ratios = np.exp(result.params)
print("\n勝算比（Odds Ratios）:")
print(odds_ratios)

# 8. 自動匯出報告為 TXT 檔
with open("logistic_regression_summary.txt", "w", encoding="utf-8") as f:
    f.write(result.summary().as_text())
    f.write("\n\n勝算比（Odds Ratios）:\n")
    f.write(str(odds_ratios))

print("✅ 報告已匯出為 logistic_regression_summary.txt")
