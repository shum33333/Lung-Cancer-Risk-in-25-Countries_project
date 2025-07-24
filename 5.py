import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# 中文字型設定
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('lung_cancer_prediction_dataset.csv')

# 分組
group_cancer = df[df["Lung_Cancer_Diagnosis"] == "Yes"]
group_noncancer = df[df["Lung_Cancer_Diagnosis"] == "No"]

# 數值欄位
numeric_features = ["Age", "Cigarettes_per_Day", "Years_of_Smoking"]

# -----------------------------------------------------
# 進行 t 檢定並印出結果，同時儲存成 list
# -----------------------------------------------------
print("\n🔍 雙樣本獨立 t 檢定結果：")

results = []

for col in numeric_features:
    t_stat, p_val = ttest_ind(
        group_cancer[col].dropna(),
        group_noncancer[col].dropna(),
        equal_var=False
    )
    significance = "具統計顯著性（p < 0.05）" if p_val < 0.05 else "不具統計顯著性（p ≥ 0.05）"

    print(f"\n【{col}】")
    print(f"  t 值 = {t_stat:.3f}")
    print(f"  p 值 = {p_val:.5f}")
    print(f"  → {significance}")

    results.append({
        "變項名稱": col,
        "t 值": round(t_stat, 3),
        "p 值": round(p_val, 5),
        "統計意義": significance
    })

# -----------------------------------------------------
# 將結果輸出到 Excel
# -----------------------------------------------------
result_df = pd.DataFrame(results)
excel_filename = "t_test_results.xlsx"
result_df.to_excel(excel_filename, index=False)
print(f"\n✅ t 檢定結果已匯出至：{excel_filename}")

# -----------------------------------------------------
# 繪圖：直方圖 + 盒鬚圖
# -----------------------------------------------------
for col in numeric_features:
    # 分布圖（histplot）
    plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x=col, hue="Lung_Cancer_Diagnosis", kde=True, palette="Set2", bins=30)
    plt.title(f"{col} 分布圖（依肺癌診斷）")
    plt.xlabel(col)
    plt.ylabel("人數")
    plt.tight_layout()
    hist_filename = f"{col}_distribution_by_diagnosis.png"
    plt.savefig(hist_filename, dpi=300)
    print(f"📊 已儲存圖檔：{hist_filename}")
    plt.show()

    # 盒鬚圖（boxplot）
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Lung_Cancer_Diagnosis", y=col, data=df, palette="Set3")
    plt.title(f"{col} 盒鬚圖（依肺癌診斷）")
    plt.xlabel("是否診斷肺癌")
    plt.ylabel(col)
    plt.tight_layout()
    box_filename = f"{col}_boxplot_by_diagnosis.png"
    plt.savefig(box_filename, dpi=300)
    print(f"📊 已儲存圖檔：{box_filename}")
    plt.show()
