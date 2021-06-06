from PIL import Image
import glob
import os
import re
import numpy as np
import scipy.stats

def pic_ave(small_img):
    color_arr = np.array(small_img)
    w_size, h_size, n_color = color_arr.shape
    color_arr = color_arr.reshape(w_size * h_size, n_color)

    color_mean = np.mean(color_arr, axis=0)
    color_mean = color_mean.astype(int)
    color_mean = tuple(color_mean)

    im = Image.new('RGB', (100, 100), color_mean)
    print(f"ave: {color_mean}")
    return im


def pic_max(small_img):
    color_arr = np.array(small_img)
    w_size, h_size, n_color = color_arr.shape
    color_arr = color_arr.reshape(w_size * h_size, n_color)
    color_code = ['{:02x}{:02x}{:02x}'.format(*elem) for elem in color_arr]
    mode, _ = scipy.stats.mode(color_code)
    r = int(mode[0][0:2], 16)
    g = int(mode[0][2:4], 16)
    b = int(mode[0][4:6], 16)
    color_mode = (r, g, b)
    im = Image.new('RGB', (100, 100), color_mode)
    print(f"max: {color_mode}")
    return im


def pic_central(small_img):
    color_arr = np.array(small_img)
    w_size, h_size, n_color = color_arr.shape
    color_arr = color_arr.reshape(w_size * h_size, n_color)
    r = [elem[0] for elem in color_arr]
    g = [elem[1] for elem in color_arr]
    b = [elem[2] for elem in color_arr]
    color_median = (int(np.median(r)), int(np.median(g)), int(np.median(b)))

    im = Image.new('RGB', (100, 100), (color_median))
    print(f"central: {color_median}")
    return im

def pic_getpixcel(small_img):
    #右端の画素を指定して色を出力
    pos = (small_img.width - 1, small_img.height - 1)
    color = small_img.getpixel(pos)
    colorstr = (f"RGB{color}")
    colorstr = re.sub("\(|\)|\s", "", colorstr)
    return colorstr

from_dir = 'ImgFile/HeroImg/'
to_dir = 'ImgFile/GenImg/'

for path in glob.glob(os.path.join(from_dir, '*.png')):
    img = Image.open(path)  # 読み込み
    basename = os.path.splitext(os.path.basename(path))[0]
    small_img = img.resize((100, 100))  # 時間短縮のために解像度を落とす
    #print(basename)
    colorstr = pic_getpixcel(small_img)
    print(basename + ',' + colorstr)
    # outputimg = Image.new('RGB', (400, 100), (255, 255, 255))

    # exe_ave = pic_ave(small_img)
    # exe_max = pic_max(small_img)
    # exe_central = pic_central(small_img)

    # outputimg.paste(small_img, (0, 0))
    # outputimg.paste(exe_ave, (100, 0))
    # outputimg.paste(exe_max, (200, 0))
    # outputimg.paste(exe_central, (300, 0))
        
    # exefilename = basename + '_OAMC.png'
    # outputimg.save(os.path.join(to_dir, exefilename))
# path = 'ImgFile/HeroImg/ui_pro_icon360.png'
# img = Image.open(path)  # 読み込み
# basename = os.path.splitext(os.path.basename(path))[0]
# small_img = img.resize((100, 100))  # 時間短縮のために解像度を落とす
# colorstr = pic_getpixcel(small_img)
# print(basename + ',' + colorstr)