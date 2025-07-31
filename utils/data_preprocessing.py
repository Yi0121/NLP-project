import re
import string
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from scipy.signal import dfreqresp

""" 如果沒下載過需要先執行一次 """
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
def clean_text(text):
    """ 對單一文字進行清洗 """
    # 1. 轉換為小寫
    text = text.lower()
    # 2. 移除html標籤
    text = re.sub(r'<.*?>', "", text)
    # 3. 移除標點符號
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 4. 移除數字
    text = re.sub(r'\d+', '', text)
    # 5. 移除多於空白
    text = re.sub(r'\s+', ' ', text).strip()
    return text
data = {'review': [
    "This is a *fantastic* movie! It's 10/10. <br /> Really enjoyed it.",
    "The plot was quite boring... (zzzzz) Will not watch again.",
    "<html>Another great film!</html> This one received 9/10 stars."
]}
df = pd.DataFrame(data)
df['clean_review'] = df['review'].apply(clean_text)
print(df[['clean_review']].head())


