# -*- coding = utf-8 -*-
# @Time : 2020/8/8 17:14
# @Author : AprilYyt
# @File : crawler2.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import bs4
from lxml import etree
import urllib.request,urllib.error
import xlwt
import re
import pandas as pd

# r = requests.get("https://www.qcc.com/elib_financing_p1.html")

def main():

    baseurl = 'https://www.qcc.com/elib_financing'
    #爬取网页 & 解析数据
    datalist = getData(baseurl)
    #二次爬取产品简介
    # datalist = getDescription(datalist)
    # print(datalist)
    #保存数据
    savepath="企查查融资情况test.csv"
    saveData(datalist,savepath)
    #askURL("https://www.qcc.com/elib_financing")

# 爬取网页
def getData(baseurl):

    datalist = []
    for i in range(1,11): #练习只爬取第一页 后面在这里更改要爬取的页面数
        url = baseurl+ '_p_' + str(i) + '.html'
        html = askURL(url)  # 保存获取到的网页源码
        parseHTML = bs4.BeautifulSoup(html, 'html.parser')
        table = parseHTML.find_all(name='tr')

        li = []

        for tr in table:
            tr_list = []
            dic = {}
            #获取所有text
            for td in tr.find_all(name='td'):
                text = td.get_text()
                #去除所有空格
                text = text.replace('\n', '')
                text = text.replace('\t', '')
                text = text.replace('\xa0', '')
                text = text.replace(' ', '')

                # print(text, type(text))
                tr_list.append(text)

            #获取所有详情链接
            for td_link in tr.find_all(name='a', href=True):
                tr_list.append(td_link['href'])

            #tr_list内容写入li
            if len(tr_list) != 0:
                dic['序号'] = tr_list[0]
                dic['产品名称'] = tr_list[2]
                dic['产品链接'] = 'https://www.qcc.com'+ tr_list[-1]
                dic['所属公司'] = tr_list[3]
                dic['投资机构'] = tr_list[4]
                dic['融资阶段'] = tr_list[5]
                dic['融资金额'] = tr_list[6]
                dic['融资时间'] = tr_list[7]

            li.append(dic)

        for dic in li:
            if len(dic)!=0:
                datalist.append(dic)

    return datalist

#二次爬取，从每个产品的详情链接里爬出产品简介
def getDescription(datalist):
    for i in range(0,len(datalist)):
        url = str(datalist[i]['产品链接'])#获取单个产品链接
        html = askURL(url)  # 获取详情网页源码
        #用bs4的方法
        parseHTML = bs4.BeautifulSoup(html, 'html.parser')
        table = parseHTML.find_all('section',id='productIntro')

        for tr in table:
            tr_list = []
            dic = {}
            # 获取所有text
            for td in tr.find_all(name='td'):
                text = td.get_text()
                # 去除空格
                text = text.replace('\n', '')
                text = text.replace('\t', '')
                text = text.replace('\xa0', '')
                text = text.replace(' ', '')
                tr_list.append(text)
            # 更新datalist
            if len(tr_list) != 0:
                dic['产品简介'] = tr_list[0]
                datalist[i].update(dic)

    return datalist

#获得指定URL的网页内容
def askURL(url):
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)

    except urllib.error.URLError as e:
        print(e)
        # if hasattr(e, "code"):
        #     # print(e.code)
        #     print(e.text)

        # if hasattr(e, "reason"):
        #     # print(e, reason)
        #     print(e.text)

    return html

# 保存数据
def saveData(datalist, savepath):
    df = pd.DataFrame(datalist)
    print(df.head())
    df.to_csv(savepath,encoding="utf_8_sig")
    return None
    #声明表头字段
    ordered_list = ['序号','产品名称','产品链接','所属公司','投资机构','融资阶段','融资金额','融资时间','产品简介']
    wb = xlwt.Workbook("New File.xlsx")
    ws = wb.add_sheet("融资信息")

    first_row = 0
    for header in ordered_list:
        col = ordered_list.index(header)  # 保持表头顺序
        ws.write(first_row, col, header)  # 写入表头

    row = 1
    for data in datalist:
        for _key, _value in data.items():  ###for key,value in dictionary.items():xxxx
            col = ordered_list.index(_key)
            ws.write(row, col, _value)
        row += 1  # enter the next row

    wb.save(savepath)

if __name__ == "__main__":

    main()