# -*- coding:utf-8 -*-
import chardet
import urllib
from urllib.request import urlopen
import re
import sys

#by rebootORZ

def getWebTitle(url):
    #print(url)
    try:
        res = urlopen(url).read()
        charset = chardet.detect(res)
        res = res.decode(charset['encoding'])
        title = re.findall('<title>(.+)</title>', res)
        if title == []:
            title = re.findall('<TITLE>(.+)</TITLE>', res)
            if title == []:
                print('访问异常，请手动验证。\n')
                output.write('访问异常，请手动验证。\n')
                #output.write(url + '  ------  ' + '访问异常，请手动验证。\n')#输出URL和标题
            else:
                print(str(title) + '\n')
                output.write(str(title) + '\n')
                #output.write(url + '  ------  ' + str(title) + '\n')
        else:
            print(str(title) + '\n')
            output.write(str(title) + '\n')
            #output.write(url + '  ------  ' + str(title) + '\n')
    except urllib.error.URLError as e:
        error = str(e)
        if "urlopen error [Errno 11001]" in error:
            print('站点无法访问\n')
            output.write('站点无法访问\n')
            #output.write(url + '  ------  ' + '站点无法访问\n')
        if "403" in error:
            print("403 Forbidden\n")
            output.write("403 Forbidden\n")
            #output.write(url + '  ------  ' + "403 Forbidden\n")
        if "SSL: CERTIFICATE_VERIFY_FAILED" in error:
            print("证书异常，需自行访问。\n")
            output.write("证书异常，需自行访问。\n")
            #output.write(url + '  ------  ' + "证书异常，需自行访问。\n")
        if "404" in error:
            print("页面404\n")
            output.write("页面404\n")
            #output.write(url + '  ------  ' + "页面404\n")
        if "WinError 10061" in error:
            print("由于目标计算机积极拒绝，无法连接。\n")
            output.write("由于目标计算机积极拒绝，无法连接。\n")
            #output.write(url + '  ------  ' + "由于目标计算机积极拒绝，无法连接。\n")
        if "WinError 10060" in error:
            print("由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。\n")
            output.write("由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。\n")
            #output.writable(url + '  ------  ' + "由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。\n")

if __name__ == '__main__':
    #print(sys.argv[1])
    file = open(sys.argv[1], 'r')
    output = open("Title.txt",'w')
    for url in file.readlines():
        url = str(url).strip()
        if 'http' not in url:
            url_1 = "http://" + url
            #url_2 = "https://" + url
            getWebTitle(url_1)
            #getWebTitle(url_2)
        else:
            getWebTitle(url)
    output.close()

