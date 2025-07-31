import json
import pandas as pd
import os

def load_csv_dataset(filepath):
    """ 讀取 csv 檔案 """
    try:
        df = pd.read_csv(filepath,encoding='utf-8')
        return df
    except UnicodeEncodeError:
        return pd.read_csv(filepath, encoding='big5')
    except Exception as e:
        print(f"無法讀取 CSV 資料集 {filepath} : {e}")
        return None

def load_json_dataset(filepath):
    """ 讀取 JSON 檔案 """
    try:
        df = pd.read_json(filepath,encoding='utf-8')
        return df
    except Exception as e:
        data = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))
        return pd.DataFrame(data)

def load_txt_dataset(filepath):
    """ 逐行讀取 TXT 檔案 """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return [line.strip() for line in lines if line.strip()]
def load_all_dataset(data_dir = 'data'):
    all_datasets = {}
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        if filename.endswith('.csv'):
            df = load_csv_dataset(filepath)
            if df is not None:
                all_datasets[filename] = df
                print(f"載入 CSV 檔案 : {filename} , 筆數 : {len(df)}")
        elif filename.endswith('.json'):
            df = load_json_dataset(filepath)
            if df is not None:
                all_datasets[filename] = df
                print(f"載入 JSON 檔案 : {filename} , 筆數 : {len(df)}")
        elif filename.endswith('.txt'):
            text = load_txt_dataset(filepath)
            if text is not None:
                all_datasets[filename] = text
                print(f"載入 TXT 檔案 : {filename} , 筆數 : {len(text)}")
        else:
            print(f"跳過不支援的檔案類型: {filename}")

    return all_datasets


