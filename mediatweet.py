import sys
from config import *
import json
from requests_oauthlib import OAuth1Session

# Twitter APIのAuthToken等は事前に用意
# OAuth認証 セッションを開始
twitter = OAuth1Session(consumer_key, consumer_secret, token, token_secret)

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# 画像 URL
imgby = open('ImgFile/GenImg/2021-06-05T13_02_26S.png','rb')
files = {"media" : imgby}
req_media = twitter.post(url_media, files = files)

# レスポンス
if req_media.status_code != 200:
    print ("画像アップロード失敗: %s", req_media.text)
    exit()

# media_id を取得
media_id = json.loads(req_media.text)['media_id']

# 投稿した画像をツイートに添付したい場合はこんな風に取得したmedia_idを"media_ids"で指定してツイートを投稿
message = 'test008'
params = {'status': message, "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)