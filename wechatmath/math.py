# coding:utf-8
import itchat
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image
import jieba

itchat.login()
friends = itchat.get_friends(update=True)[0:]
tList = []
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    tList.append(signature)

# 拼接字符串
text = "".join(tList)

#jieba分词

wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

#wordcloud词云

d = os.path.dirname(__file__)
# 更改目录下Wordcloud生成图片，如：xiaohuangren.jpg
alice_coloring = np.array(Image.open(os.path.join(d, "wechat.jpg")))
# win系统需要更改font路径
my_wordcloud = WordCloud(width=1920, height=1080, background_color="black", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42,
                         font_path='.\STXINWEI.TTF')\
    .generate(wl_space_split)

image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

# 保存图片 并发送到手机
my_wordcloud.to_file(os.path.join(d, "wechat_cloud.jpg"))
itchat.send_image("wechat_cloud.jpg", 'filehelper')

