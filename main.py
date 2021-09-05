#coding: UTF-8
import json
import io
import random as rnd
from requests_oauthlib import OAuth1Session
from PIL import Image, ImageDraw
from datetime import datetime
from twitter import *
from config import *

#実行スクリプトパスに移動する
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

twitter = OAuth1Session(consumer_key, consumer_secret, token, token_secret)
url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

print("=====Deck_Generate_Start=====")
#Card.jsonを取得
with open("Card.json","r") as c:
    Cardjn = json.load(c)
print("-Open_Card.json...")

#Hero.jsonを取得
with open("Hero.json","r") as h:
    Herojn = json.load(h)
print("-Open_Hero.json...")

# 現在の時間を取得する
choiceCard = (datetime.datetime.today()).hour
j = 0

# 1:恒常カードのみ
if choiceCard == 1:
    print("Now CardChoise is....[Constancy]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['source'] == 'Constancy'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)
    SetCardjn = changecard

# コラボカードのみ
elif choiceCard == 2:
    print("Now CardChoise is....[Collabo]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['source'] == 'Collabo'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)
    SetCardjn = changecard
    
# イベントカードのみ
elif choiceCard == 3:
    print("Now CardChoise is....[event]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['source'] == 'event'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)   
    SetCardjn = changecard

# Rカードのみ
elif choiceCard == 4:
    print("Now CardChoise is....[R]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['rarity'] == 'r'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)       
    SetCardjn = changecard

# SRカードのみ
elif choiceCard == 5:
    print("Now CardChoise is....[SR]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['rarity'] == 's'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)    
    SetCardjn = changecard

# URカードのみ
elif choiceCard == 6:
    print("Now CardChoise is....[UR]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['rarity'] == 'u'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)    
    SetCardjn = changecard

# Redカードのみ
elif choiceCard == 7:
    print("Now CardChoise is....[Red]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['color'] == 'red'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)    
    SetCardjn = changecard

# Blueカードのみ
elif choiceCard == 8:
    print("Now CardChoise is....[Blue]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['color'] == 'blue'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)    
    SetCardjn = changecard

# Greenカードのみ
elif choiceCard == 9:
    print("Now CardChoise is....[Green]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['color'] == 'green'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)    
    SetCardjn = changecard

# UR,SRの恒常カードのみ
elif choiceCard == 10:
    print("Now CardChoise is....[Constancy-UR-SR]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['source'] == 'Constancy'), None)
    changecard_s = next((changecard for changecard in j if changecard['rarity'] == 's') , None)
    changecard_u = next((changecard for changecard in j if changecard['rarity'] == 'u'), None)
    rnd.shuffle(changecard_s,changecard_u,Herojn)
    SetCardjn = [changecard_u[0],changecard_u[1],changecard_s[0],changecard_s[1]]

# URカード恒常のみ
elif choiceCard == 11:
    print("Now CardChoise is....[Constancy-UR]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['rarity'] == 'u' and Cardjn['source'] == 'Constancy' ), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)
    SetCardjn = changecard    

# 恒常,コラボあり,SR,UR揃ったやつ
elif choiceCard == 12:
    print("Now CardChoise is....[Constancy-Collabo-SR-UR-RBG]")
    changecard = next((Cardjn for Cardjn in j if Cardjn['source'] == 'Constancy' or Cardjn['source'] == 'Collabo'), None)
    changecard = next((changecard for changecard in j if changecard['rarity'] == 's' or changecard['rarity'] == 'u'), None)
    rnd.shuffle(changecard)
    rnd.shuffle(Herojn)
    SetCardjn = changecard    

# なんでも
else:
    print("Now CardChoise is....[Random]")
    rnd.shuffle(Cardjn)
    rnd.shuffle(Herojn)

    # Card OR changecard SET
    SetCardjn = Cardjn


def setjnlist( Herojn,Cardjn ):
    # リストの末尾の要素を取得してかつ母集団から削除
    Hero = Herojn.pop()
    deck1 = Cardjn.pop()  
    deck2 = Cardjn.pop()
    deck3 = Cardjn.pop()
    deck4 = Cardjn.pop()
    print("-pop_list:" + Hero["hero"] + "," + deck1["card"] + "," + deck2["card"] + ","+ deck3["card"] + "," + deck4["card"])
    im1 = Image.open('ImgFile/CardImg/' + deck1["img"]).convert('RGBA')
    im2 = Image.open('ImgFile/CardImg/' + deck2["img"]).convert('RGBA')
    im3 = Image.open('ImgFile/CardImg/' + deck3["img"]).convert('RGBA')
    im4 = Image.open('ImgFile/CardImg/' + deck4["img"]).convert('RGBA')
    im5 = Image.open('ImgFile/HeroImg/' + Hero["img"]).convert('RGBA')
    iconimg = Image.open('ImgFile/deck_logowhite.png').convert('RGBA')
    logoimg = Image.open('ImgFile/deckcps_mark.png').convert('RGBA')
    im5_RGB = (int(Hero["R"]),int(Hero["G"]),int(Hero["B"]))
    print("-ImgOpen_R:" + Hero["R"] + "_G:" + Hero["G"] + "_B:" + Hero["B"])
    Setjn = [Hero,deck1,deck2,deck3,deck4,im1,im2,im3,im4,im5,iconimg,logoimg,im5_RGB]

    return (Setjn)


#costom
def get_concat_s(im1,im2,im3,im4,im5,iconimg,logoimg,im5_RGB):
    print("======Imgmerge_Start=====")
    #image set
    bg = Image.new('RGBA',(1478,1970),(im5_RGB[0], im5_RGB[1], im5_RGB[2]))
    dst = Image.new('RGBA',(im1.width * 2 ,im1.height * 2))
    subdst = Image.new('RGBA',(im5.width,im5.height))
    iconimg_clear = Image.new("RGBA", dst.size, (255, 255, 255, 0))
    logoimg_clear = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    iconimg_size = Image.new("RGBA",(iconimg.width,iconimg.height),(255, 255, 255, 0))
    
    #"bg" coler paint
    draw = ImageDraw.Draw(bg)

    #paste to logo,icon
    logoimg_clear.paste(logoimg, (930, 1870))
    iconimg_size.paste(iconimg,(0,0))
    iconimg_size = iconimg_size.resize((iconimg.width*3,iconimg.height*3))
    mask = iconimg_size.copy()
    iconimg_size.putalpha(76) #image Transmittance change to 30%
    iconimg_clear.paste(iconimg_size,(im1.width - 440,im1.height - 549),mask)
    
    #4Card merge
    dst.paste(im1,(0,0))
    dst.paste(im2,(im1.width,0))
    dst.paste(im3,(0,im1.height))
    dst.paste(im4,(im1.width,im1.height))

    #hero icon merge
    subdst.paste(im5,(0,0))
    subdst = subdst.resize((int(im5.width*1.5),int(im5.height*1.5)))
    
    #merge dst to icon
    dst = Image.alpha_composite(dst,iconimg_clear)

    #merge bg to 4Card
    bg.paste(dst,(0+116,0+64))

    #merge bg to heroicon
    bg.paste(subdst,(0+116,dst.height+64))
    
    #merge bg to logo
    bg = Image.alpha_composite(bg, logoimg_clear)
    print("======Imgmerge_sucsess!=====")

    return bg

Setjn = setjnlist(Herojn,SetCardjn)

#Hero["hero"]でヒーロー名,Hero["img"]でヒーロー画像を表示出来る。Cardも同様
Tweetmsg = ("【" + Setjn[0]["hero"] + "】" + "で\n" + "\n" + "・"+ Setjn[1]["card"] + "\n" + "・"+ Setjn[2]["card"] + "\n" + "・"+ Setjn[3]["card"] + "\n" + "・"+ Setjn[4]["card"] + "\n" + "\nを使ったデッキ")
print("-Generate_msg"+"\n"+f"{Tweetmsg}")

#生成した画像をバイナリ変換してTwitterにupload
timestr = datetime.now().isoformat(timespec='seconds')
out_img = io.BytesIO()
get_concat_s(Setjn[5],Setjn[6],Setjn[7],Setjn[8],Setjn[9],Setjn[10],Setjn[11],Setjn[12]).save(out_img,format='PNG')
img_byte = out_img.getvalue()

# 画像 URL
files = {"media" : img_byte}
send_media = twitter.post(url_media, files = files)
print("-upload_to_media_for_Twitter")
# レスポンス
if send_media.status_code != 200:
    print ("@@@@Upload Faild@@@@: %s", send_media.text)
    exit()

# media_id を取得
media_id = json.loads(send_media.text)['media_id']
print(f"-get_media_id:{media_id}")

# 投稿した画像をツイートに添付したい場合はこんな風に取得したmedia_idを"media_ids"で指定してツイートを投稿
params = {'status': Tweetmsg, "media_ids": [media_id]}
send_media = twitter.post(url_text, params = params)
print("=====tweet_sucsess!! ('A')=====")