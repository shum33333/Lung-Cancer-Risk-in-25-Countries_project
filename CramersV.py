import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# 設定中文字型（避免圖表中文字變亂碼）
plt.rcParams['font.family'] = 'Microsoft JhengHei'  # Windows 可用微軟正黑體，mac 可用 'Arial Unicode MS'

# 讀取資料
df = pd.read_csv(r"D:\shan\power-bi_advanced-courses\Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv", encoding='utf-8')

# 定義 Cramér's V 計算函數
def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))

# 計算 Cramér's V
cv1 = cramers_v(df['Smoker'], df['Lung_Cancer_Diagnosis'])
cv2 = cramers_v(df['Gender'], df['Adenocarcinoma_Type'])

print("吸菸者與肺癌診斷的 Cramér's V:", round(cv1, 3))
print("性別與腺癌類型的 Cramér's V:", round(cv2, 3))

# 畫圖：吸菸者 vs 肺癌診斷
plt.figure(figsize=(8, 5))
pd.crosstab(df['Smoker'], df['Lung_Cancer_Diagnosis']).plot(
    kind='bar', stacked=True, colormap='Set2', rot=0)
plt.title("吸菸與肺癌診斷的交叉表", fontsize=14)
plt.xlabel("是否吸菸")
plt.ylabel("人數")
plt.legend(title="肺癌診斷")
plt.tight_layout()
plt.show()

# 畫圖：性別 vs 腺癌類型
plt.figure(figsize=(8, 5))
pd.crosstab(df['Gender'], df['Adenocarcinoma_Type']).plot(
    kind='bar', stacked=True, colormap='Set3', rot=0)
plt.title("性別與腺癌類型的交叉表", fontsize=14)
plt.xlabel("性別")
plt.ylabel("人數")
plt.legend(title="腺癌診斷")
plt.tight_layout()
plt.show()
