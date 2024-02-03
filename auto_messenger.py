import jpholiday
import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # .envファイルから環境変数を読み込む

# 今日の日付
today = datetime.date.today()

# 今日が祝日かどうかをチェック
if jpholiday.is_holiday(today):
    holiday_name = jpholiday.is_holiday_name(today)
    print(f"Today ({today}) is a holiday in Japan: {holiday_name}")
else:
  # トークン
  token = os.getenv('SLACK_TOKEN')

  # 送信するメッセージ
  message = os.getenv('SLACK_MESSAGE')

  # チャンネルID
  channel = os.getenv('SLACK_CHANNEL')

  # Slack APIエンドポイント
  url = "https://slack.com/api/chat.postMessage"

  # ヘッダー
  headers = {
      "Authorization": f"Bearer {token}",
      "Content-Type": "application/json"
  }

  # リクエストボディ
  data = {
      "channel": channel,
      "text": message
  }

  # POSTリクエストでSlackにメッセージを送信
  response = requests.post(url, headers=headers, json=data)

  # レスポンス確認
  print('Response: ' + str(response.text))
  print('Response code: ' + str(response.status_code))
