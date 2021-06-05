import os

#更新後 source ~/.bashrc を忘れずに
app_name = "DeckCps tester" # 上で作成したアプリケーション名
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET_KEY")
token = os.environ.get("TWITTER_TOKEN")
token_secret = os.environ.get("TWITTER_TOKEN_SECRET")