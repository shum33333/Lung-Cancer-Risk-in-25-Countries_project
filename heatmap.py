import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 匯入資料
data = pd.read_csv('D:/shan/power-bi_advanced-courses/Lung-Cancer-Risk-in-25-Countries_project/lung_cancer_prediction_dataset.csv')
df = data.copy()

# 顯示前五筆資料
print(df.head())
df.info()

# 定義函式：繪製數值欄位之間的相關係數熱力圖
def plot_correlation_heatmap(df):
    """繪製數值特徵的相關係數熱力圖"""
    corr_matrix = df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()

# 選出數值型欄位並繪圖
num_cols = df.select_dtypes(include='number').columns
plot_correlation_heatmap(df[num_cols])
