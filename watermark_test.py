import time
import cv2
from core import WaterMark

bwm = WaterMark(password_img=1, password_wm=1)
bwm.read_img('pic/ori_img.jpeg')
wm = '123'
t1 = time.time()
bwm.read_wm(wm, mode='str')
bwm.embed('output/embedded.png')
t2 = time.time()
print('加水印时间消耗 = ' + str((t2-t1)* 1000))

len_wm = len(bwm.wm_bit)  # 解水印需要用到长度
print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))


ori_img_shape = cv2.imread('pic/ori_img.jpeg').shape[:2]# 抗攻击有时需要知道原图的shape
t1 = time.time()
#解水印
bwm1 = WaterMark(password_img=1, password_wm=1)
wm_extract = bwm1.extract('output/embedded.png', wm_shape=14, mode='str')
print("不攻击的提取结果：", wm_extract)
t2 = time.time()
print('解水印时间消耗 = ' + str((t2-t1)* 1000))