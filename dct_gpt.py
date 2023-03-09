import numpy as np
from scipy.fftpack import dct, idct
import cv2
import time
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def embed_watermark(img, watermark):
    # binary_data = bin(int(watermark.encode('utf-8').hex(), base=16))[2:]
    binary_data = ''.join(format(ord(i), '08b') for i in watermark)
    row, col = img.shape
    blocks = [img[i:i+8, j:j+8] for i in range(0, row, 8) for j in range(0, col, 8)]
    dct_blocks = [dct2(block) for block in blocks]
    watermark_array = np.array([int(bit) for bit in binary_data])
    for i, block in enumerate(dct_blocks):
        if i < len(watermark_array):
            block[0, 0] = block[0, 0] + watermark_array[i]
        else:
            break
    watermarked_blocks = [idct2(block) for block in dct_blocks]
    watermarked_img = np.zeros(img.shape)
    k = 0
    for i in range(0, row, 8):
        for j in range(0, col, 8):
            watermarked_img[i:i+8, j:j+8] = watermarked_blocks[k]
            k += 1
    return watermarked_img

def extract_watermark(img, watermark_length):
    row, col = img.shape
    blocks = [img[i:i+8, j:j+8] for i in range(0, row, 8) for j in range(0, col, 8)]
    dct_blocks = [dct2(block) for block in blocks]
    watermark_array = []
    for block in dct_blocks:
        watermark_array.append(int(round(block[0, 0])) % 2)
    watermark_bits = ''.join([str(bit) for bit in watermark_array])
    watermark = ''.join(chr(int(watermark_bits[i:i+8], 2)) for i in range(0, len(watermark_bits), 8))
    watermark_unicode = watermark.encode('unicode_escape').decode('utf-8')
    return watermark_unicode[:watermark_length]

# 读取原始图像
img = cv2.imread('pic/ori_img.jpeg', cv2.IMREAD_GRAYSCALE)
t1 = time.time()
# 嵌入水印
watermarked_img = embed_watermark(img, 'Hello, world!')
t2 = time.time()
print('加水印时间消耗 = ' + str((t2-t1)* 1000))
# 保存水印图像
cv2.imwrite('watermarked.png', watermarked_img)

# 读取水印图像
watermarked_img = cv2.imread('watermarked.png', cv2.IMREAD_GRAYSCALE)

t1 = time.time()
# 提取水印
watermark = extract_watermark(watermarked_img, len('Hello, world!'))
t2 = time.time()
print('提取水印时间消耗 = ' + str((t2-t1)* 1000))
print(watermark)