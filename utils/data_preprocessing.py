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
def stop_words(text):
    """ 移除停用詞 """
    # 分詞
    tokens = nltk.word_tokenize(text)
    # 停用詞
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens
def lemmatize(tokens):
    """ 還原詞型 """
    lemmatizer = WordNetLemmatizer()
    lemma = [lemmatizer.lemmatize(token) for token in tokens]
    return lemma

