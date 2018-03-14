
import multidict as multidict

import numpy as np
import time

import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be",text):
            continue
        val = tmpDict.get(text,0)
        tmpDict[text.lower()] = val+1
    for key in tmpDict:
        fullTermsDict.add(key,tmpDict[key])
    return fullTermsDict



def makeImage(text):
    alice_mask = np.array(Image.open("alice_mask.png"))

   #background_color:设置图片背景色；max_words：设置图片能容纳的最大词数；mask：设置词云样式   
    wc = WordCloud(background_color="white", max_words=1000, mask=alice_mask)
    # 生成词云
    wc.generate_from_frequencies(text)

    # 展示
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

d = path.dirname(__file__)

text = open(path.join(d, 'alice.txt'),encoding='utf-8')
text = text.read()
makeImage(getFrequencyDictForText(text))