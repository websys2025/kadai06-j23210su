import requests
import json

# データ名称：気象庁天気予報
# 概要：東京都の当日・翌日・翌々日の天気予報を取得する
# 取得形式：JSON形式
# エンドポイント：https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json
# 地域コード：130000（東京都）
# 機能：東京地方の天気情報（晴れ・曇り・雨など）を取得して表示
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

# APIにリクエストを送り、JSONデータを取得
response = requests.get(url)
forecast_json = response.json()

# JSONから東京地方の天気予報部分を抽出
tokyo_weather = forecast_json[0]["timeSeries"][0]["areas"][0]

# 東京地方と、天気情報と予報日時を取得
area_name = tokyo_weather["area"]["name"]
weathers = tokyo_weather["weathers"]
dates = forecast_json[0]["timeSeries"][0]["timeDefines"]

print(f"地域：{area_name}\n")
for i in range(len(weathers)):
    print(f"{dates[i]} の予報：{weathers[i]}")

