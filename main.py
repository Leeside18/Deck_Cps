#coding: UTF-8
import os
import json
import random as rnd
from PIL import Image, ImageDraw
from datetime import datetime
from twitter import *
from config import *

Tweetmsg = ""

#Card.jsonを取得
with open("Card.json","r") as c:
    Cardjn = json.load(c)

#Hero.jsonを取得
with open("Hero.json","r") as h:
    Herojn = json.load(h)

#要素の並び順をシャッフル→先頭4列を取得する
rnd.shuffle(Cardjn)
rnd.shuffle(Herojn)

# リストの末尾の要素を取得してかつ母集団から削除
Hero = Herojn.pop()
deck1 = Cardjn.pop()  
deck2 = Cardjn.pop()
deck3 = Cardjn.pop()
deck4 = Cardjn.pop()

im1 = Image.open('ImgFile/CardImg/' + deck1["img"]).convert('RGBA')
im2 = Image.open('ImgFile/CardImg/' + deck2["img"]).convert('RGBA')
im3 = Image.open('ImgFile/CardImg/' + deck3["img"]).convert('RGBA')
im4 = Image.open('ImgFile/CardImg/' + deck4["img"]).convert('RGBA')
im5 = Image.open('ImgFile/HeroImg/' + Hero["img"]).convert('RGBA')
iconimg = Image.open('ImgFile/deck_logowhite.png').convert('RGBA')
logoimg = Image.open('ImgFile/deckcps_mark.png').convert('RGBA')
im5_RGB = (int(Hero["R"]),int(Hero["G"]),int(Hero["B"]))

#Hero["hero"]でヒーロー名,Hero["img"]でヒーロー画像を表示出来る。Cardも同様
print("【" + Hero["hero"] + "】" + "で\n" + "\n" + "・"+ deck1["card"] + "\n" + "・"+ deck2["card"] + "\n" + "・"+ deck3["card"] + "\n" + "・"+ deck4["card"] + "\n" + "\nを使ったデッキ")
# t = Twitter(
#     auth=OAuth(
#         token,
#         token_secret,
#         consumer_key,
#         consumer_secret,
#     )
# )
# t.statuses.update(status="Tweetmsg")

#costom
def get_concat_s(im1,im2,im3,im4,im5,iconimg,logoimg,im5_RGB):

    #image set
    bg = Image.new('RGBA',(1246,1970),(im5_RGB[0], im5_RGB[1], im5_RGB[2]))
    dst = Image.new('RGBA',(im1.width * 2 ,im1.height * 2))
    subdst = Image.new('RGBA',(im5.width,im5.height))
    iconimg_clear = Image.new("RGBA", dst.size, (255, 255, 255, 0))
    logoimg_clear = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    iconimg_size = Image.new("RGBA",(iconimg.width,iconimg.height),(255, 255, 255, 0))
    
    #"bg" coler paint
    draw = ImageDraw.Draw(bg)

    #paste to logo,icon
    logoimg_clear.paste(logoimg, (510, 1780))
    iconimg_size.paste(iconimg,(0,0))
    iconimg_size = iconimg_size.resize((iconimg.width*3,iconimg.height*3))
    mask = iconimg_size.copy()
    iconimg_size.putalpha(76) #image Transmittance change to 30%
    iconimg_clear.paste(iconimg_size,(im1.width - 440,im1.height - 549),mask)
    
    #4Card marge
    dst.paste(im1,(0,0))
    dst.paste(im2,(im1.width,0))
    dst.paste(im3,(0,im1.height))
    dst.paste(im4,(im1.width,im1.height))

    #hero icon marge
    subdst.paste(im5,(0,0))
    subdst = subdst.resize((im5.width*2,im5.height*2))
    
    #Marge dst to icon
    dst = Image.alpha_composite(dst,iconimg_clear)

    #Marge bg to 4Card
    bg.paste(dst,(0,0))

    #Marge bg to heroicon
    bg.paste(subdst,(0,dst.height))
    
    #Marge bg to logo
    bg = Image.alpha_composite(bg, logoimg_clear)

    return bg

timestr = datetime.now().isoformat(timespec='seconds')
get_concat_s(im1,im2,im3,im4,im5,iconimg,logoimg,im5_RGB).save('ImgFile/GenImg/' + timestr + 'S' +'.png')