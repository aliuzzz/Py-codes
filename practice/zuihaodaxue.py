#!/usr/bin/python3
#coding=utf-8

#1、从网络上获取大学排名的网页内容getHTMLText()
#2、提取网页内容中信息到合适的数据结构fillUnivList()

import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        #产生异常信息
        r.raise_for_status()
        #修改编码
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    #解析
    soup = BeautifulSoup(html, "html.parser")
    #找到tbody标签
    for tr in soup.find('tbody').children:
        #找到tbody下的tr标签
        if isinstance(tr, bs4.element.Tag):
            #找到td标签，并将内容赋到列表里
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])
    pass

def printUnivList(ulist, num):
    tplt = "{0:^8}\t{1:{3}^10}\t{2:^9}"#{3}指填充时运用第三个来填充
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))

    # print("Suc"+str(num))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    #将url转换为html
    html = getHTMLText(url)
    #放入uinfo的变量中
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 30) #列出20所

main()



