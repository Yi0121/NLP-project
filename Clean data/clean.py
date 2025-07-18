import pandas as pd
import numpy as np

df = pd.read_csv('台灣各地區消費娛樂性產品(缺少24年資料).csv')
df = df.rename(columns={
    '1.食品及非酒精飲料' : '食品食品及非酒精飲料',
    '2.酒精飲料' : '酒精飲料',
    '3.菸草' : '菸草',
    '4.衣著及鞋類' : '衣著及鞋類',
    '5.住屋及水電瓦斯等費用' : '住屋及水電瓦斯等費用',
    '6.家具設備及家務服務' : '家具設備及家務服務',
    '7.醫療保健' : '醫療保健',
    '8.交通及通訊' : '交通及通訊',
    '9.休閒與文化' : '休閒與文化',
    '10.教育' : '教育',
    '11.餐廳及旅館' : '餐廳及旅館',
    '12.什項消費' : '什項消費',
    '(1)套裝旅遊(不含自助旅遊)': '套裝旅遊',
    '(2)娛樂消遣及文化服務': '娛樂消遣及文化服務',
    '(3)書報雜誌文具': '書報雜誌文具',
    '(4)教育消遣康樂器材及其附屬品': '教育消遣康樂器材及其附屬品'

})
# dftest = pd.melt(
#    df,
#    id_vars=['年份','地區'],
#    value_vars=['套裝旅遊', '娛樂消遣及文化服務', '書報雜誌文具','教育消遣康樂器材及其附屬品'],
#    var_name = '休閒與文化類別',  # 新的變數欄位名稱
#    value_name = '類別金額')
# dftest.to_csv("娛樂分類各系項樞紐.csv", index = False)
Region = df['地區'].unique().tolist()
data = {
    'RegionID' : list(range(1, len(Region) + 1)),
    'RegionName' : Region
}

north_regions = ['台北市', '新北市', '基隆市', '桃園市', '新竹市', '新竹縣', '宜蘭縣']
central_regions = ['台中市', '苗栗縣', '彰化縣', '南投縣', '雲林縣']
south_regions = ['台南市', '高雄市', '屏東縣', '嘉義市', '嘉義縣']
east_regions = ['花蓮縣', '台東縣']
island_regions = ['澎湖縣']

conditions = [
    df['地區'].isin(north_regions),
    df['地區'].isin(central_regions),
    df['地區'].isin(south_regions),
    df['地區'].isin(east_regions),
    df['地區'].isin(island_regions)
]

# 3. 定義對應的選擇列表 (當條件滿足時要賦予的值)
choices = ['北部', '中部', '南部', '東部', '離島']

df['區域'] = np.select(conditions, choices, default='未分類')
df.to_csv("區域消費.csv", index=False)


