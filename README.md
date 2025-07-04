# NLP-project : Sentiment Analysis
## 專案概述
本專案旨在開發一個情緒分析（Sentiment Analysis）模型，通過自然語言處理（NLP）技術對文本進行分類，並判斷文本中的情緒是正向、負向還是中立。本專案將使用開放資料集並運用深度學習技術（如LSTM、BERT等）來進行情緒分析。
## 功能
- 進行文本情緒分類，支持正向、負向、中立情緒標註
- 支援簡單的網頁介面，用戶可以輸入文本並查看情緒分析結果
- 支援模型訓練與評估，並展示模型的準確率、精確度等指標
## 技術堆疊
- Python
- NLP工具：NLTK、spaCy、transformers（Hugging Face）
- 深度學習框架：TensorFlow / PyTorch
- 資料處理：Pandas、NumPy
- 資料集：IMDB 影評資料集、Twitter Sentiment Dataset、Amazon Product Review
## 文件結構
```
nlp-sentiment-analysis/
├── data/                # 資料集存放資料夾
├── models/              # 保存訓練好的模型
├── app.py               # 使用 Streamlit 顯示Web介面
├── train.py             # 訓練模型
├── predict.py           # 進行情緒預測
├── evaluate.py          # 模型評估腳本
├── requirements.txt     # 依賴包清單
├── README.md            # 項目的說明文件
└── utils/               # 工具程式 (如資料處理、模型構建等)
```
## 使用方法
### 訓練模型
1. 在 ```train.py``` 中選擇要使用的模型架構（例如，LSTM、BERT等）
2. 提供資料集的路徑或使用預設資料集
3. 訓練並保存模型
### 進行預測
1. 執行 ```pridict.py```
2. 提供一段文本，模型將返回其情緒（正向、負向或中立）
### 評估指標
- 準確性(Accurary)：分類模型預測正確的比例
- 精準性(Precision)：正向情緒預測中有多少是正確的
- 召回率(Recall)：實際正向情緒中有多少被預測為正向
- F1分數：精確度和召回率的加權平均，適合類別不平衡的情況
## 版權
本專案遵循 MIT License
