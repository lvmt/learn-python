#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""学习词云的使用 
"""

"""
配置文件对象参数
加载词云文本
输出词云文件
""" 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib as plt
import numpy as np
from PIL import Image
import matplotlib.pylab as plt 
import random

# # test1
# w = WordCloud() 
# w.generate('python and wordcloud')      # 向对象中加载文本txt
# w.to_file('cloud1.png')         # 输出

# test 2
# f = open('test1.txt', 'r').read()
# f = f.lower()
# wd = WordCloud(background_color='white', width=800, height=660, margin=2).generate(f) 
# wd.to_file('test1.png')
# plt.axis('off')
# plt.imshow(wd, interpolation='bilinear')
# plt.show()  

# test3  使用mask参数，绘制圆形图片
# f = open('test1.txt', 'r').read()
# f = f.lower()
# x, y = np.ogrid[:500, :500]
# mask = (x - 150) ** 2 + (y - 150) ** 2 > 230 ** 2
# mask = 255 * mask.astype(int)
# wd = WordCloud(background_color="white", mask=mask).generate(f)
# plt.axis('off')
# plt.imshow(wd, interpolation='bilinear')
# plt.show()


"""利用背景图片，生成指定形状的词云图片
"""
# # test4 Using a mask you can generate wordclouds in arbitrary shapes.
# f = open('test1.txt', 'r').read()
# f = f.lower()
# #alice_mask = np.array(Image.open('mask.png'))

# stopwords = set(STOPWORDS)
# stopwords.add('said')
# wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask,\
#     stopwords=stopwords, contour_width=3, contour_color='steelblue').generate(f)
# wc.to_file('mask1.png')

# # show
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.figure()
# #plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
# plt.imshow(alice_mask,  interpolation='bilinear')
# plt.axis("off")
# plt.show()
 
## 上面的效果不是很好
# f = open('test1.txt', 'r').read()
# f = f.lower()
# # set mask
# photo_coloring = plt.imread('mask3.jpeg')
# w = WordCloud(background_color='green',  mask=photo_coloring, \
#     scale=1.5).generate(f)
# # show
# plt.imshow(w, interpolation='bilinear')
# plt.axis('off')
# plt.show()



""" Image-colored wordcloud
"""
f = open('test1.txt', 'r').read()
f = f.lower() 
alice_coloring = np.array(Image.open('mask3.jpeg'))
stopwords = set(STOPWORDS)
stopwords.add('said')

wc = WordCloud(background_color='white', max_words=2000, mask=alice_coloring, \
    stopwords=stopwords).generate(f)

# # create coloring from image
#image_color = ImageColorGenerator(alice_coloring)

# # show
# fig, axes = plt.subplots(1, 3)
# axes[0].imshow(wc, interpolation='bilinear')

# # recolor wordcloud and show
# axes[1].imshow(wc.recolor(color_func=image_color), interpolation='bilinear')
# axes[2].imshow(alice_coloring, cmap=plt.cm.gray, interpolation='bilinear')
# # for ax in axes:
# #     ax.set_axis_off()
# # plt.show()  

plt.imshow(wc, interpolation='bilinear') 
# plt.imshow(wc.recolor(color_func=image_color), interpolation='bilinear') 
# plt.imshow(alice_coloring, interpolation='bilinear')
plt.axis('off')
plt.show()

# 
 









"""wordcloud_cli

命令行操作模式
wordcloud_cli --text  test.txt  --imagefile test.png
wordcloud_cli -h 查看具体用法
"""



doc = """ wordcloud

width：指定图片宽度
heigh：指定图片高度
min_font_size：最小字号
max_font_size：最大字号
font_step：词语步进
font_path：指定字体路径
max_words：最大单词量
stop_words：不显示的单词
mask：指定词云形状
background_color：背景颜色
"""