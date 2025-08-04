<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>從數據看肺癌風險</title>
  <style>
    body {
      font-family: "Noto Sans TC", sans-serif;
      margin: 2em;
      line-height: 1.8;
      background-color: #f7f9fc;
      color: #333;
    }
    h1 {
      color: #0033ff;
      font-size: 2.5em;
    }
    h2 {
      color: #2c3e50;
      margin-top: 2em;
    }
    img {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 1em 0;
    }
    .section {
      margin-bottom: 2.5em;
      padding-bottom: 1em;
      border-bottom: 1px solid #ccc;
    }
  </style>
</head>
<body>

  <h1>從數據看肺癌風險</h1>
  <h3>25國家之人口特徵與環境因子分析</h3>

  <div class="section">
    <h2>📘 專題說明</h2>
    <p>本研究使用 Kaggle 平台提供的「Lung cancer Risk in 25 Countries」資料集，涵蓋來自全球 25 個國家的 22 萬筆人口樣本，資料包含年齡、性別、吸菸狀況、家族病史、環境污染、醫療可近性與肺癌診斷結果等變項。我們透過 Python 與 Power BI 進行視覺化、描述統計、t 檢定、卡方分析與羅吉斯迴歸建模，探索肺癌風險因子。</p>
  </div>

  <div class="section">
    <h2>🎯 分析目的</h2>
    <ul>
      <li>分析影響肺癌風險的生理與環境因素</li>
      <li>比較開發中國家與已開發國家之差異</li>
      <li>運用 Power BI 與 Python 呈現資料分析結果</li>
      <li>作為肺癌預防政策與健康教育的建議依據</li>
    </ul>
  </div>

  <div class="section">
    <h2>📊 資料視覺化（封面圖）</h2>
    <img src="封面圖路徑/從數據看肺癌風險_title.png" alt="從數據看肺癌風險 封面圖">
  </div>

  <div class="section">
    <h2>📄 研究摘要 PDF</h2>
    <p><a href="從數據看肺癌風險：25國家之人口特徵與環境因子分析_20250804版-1.pdf" target="_blank">🔗 點我下載完整報告 PDF</a></p>
  </div>

  <div class="section">
    <h2>📌 分析方法與結果</h2>
    <ul>
      <li>📈 使用 Cramér’s V 衡量性別與肺癌類型之關聯</li>
      <li>📊 執行卡方檢定找出顯著變項（吸菸顯著）</li>
      <li>📉 雙樣本獨立 t 檢定顯示吸菸年數與每日吸菸量皆顯著</li>
      <li>📐 邏輯斯迴歸顯示吸菸者罹癌機率為非吸菸者 3.6 倍</li>
    </ul>
  </div>

  <div class="section">
    <h2>🏥 公共衛生建議</h2>
    <ul>
      <li>戒菸為最有效的肺癌預防方式</li>
      <li>建議高風險者定期接受 LDCT 肺癌篩檢</li>
      <li>推廣國健署補助政策與戒菸服務</li>
    </ul>
  </div>

  <div class="section">
    <h2>🙋 作者資訊</h2>
    <p>李芳珊｜2025 Python 與資料分析實作</p>
  </div>

</body>
</html>




