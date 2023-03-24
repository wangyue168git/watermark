import time
import cv2
from core import WaterMark

from PIL import Image


import random
import string

def generate_random_string(length):
    # 生成包含所有大小写字母和数字的字符集
    characters = string.ascii_letters + string.digits
    # 从字符集中随机选择 length 个字符，并拼接成字符串返回
    return ''.join(random.choice(characters) for i in range(length))


test_path = 'pic/31187603.png'
test_count = 1
test_wm_len = 100

# 打开图片文件
image = Image.open(test_path)

# 获取图片的宽度和高度
width, height = image.size

# 输出图片的宽度和高度
print("图片的宽度为：", width, "像素")
print("图片的高度为：", height, "像素")

if __name__ == '__main__':
    bwm = WaterMark(password_img=1, password_wm=1,mode='multiprocessing')
    bwm.read_img(test_path)
    wm = generate_random_string(test_wm_len)
    print('水印：' + wm)
    bwm.read_wm(wm, mode='str')
    t1 = time.time()
    for i in range(test_count):
        # bwm.embed('output/embedded.png')
        bwm.embed('output/embedded.png')
    t2 = time.time()
    print('加水印时间消耗 = ' + str((t2-t1)* 1000/test_count))

    len_wm = len(bwm.wm_bit)  # 解水印需要用到长度
    print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))


    #解水印
    bwm1 = WaterMark(password_img=1, password_wm=1,mode='multiprocessing')
    t1 = time.time()
    for i in range(test_count):
        wm_extract = bwm1.extract('output/embedded.png', wm_shape=len_wm, mode='str')
    t2 = time.time()
    print("不攻击的提取结果：", wm_extract)
    print('解水印时间消耗 = ' + str((t2-t1)* 1000/test_count))
