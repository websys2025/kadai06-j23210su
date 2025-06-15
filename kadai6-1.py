import requests
import json
# データ種別：平成27年国勢調査就業状態等基本集計
# 機能 ：全国の就業状態
APP_ID = "9f0f51e9cdfbeb9766ead4d2b2235f15cc5de150"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003009692",# 就業状態
    "cdArea":"00000",# 全国
    "cdCat01": "00000",# 就業者数
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(json.dumps(data, indent=2, ensure_ascii=False))