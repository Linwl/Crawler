#!usr/bin/env python
#coding:utf-8

import re
import urllib

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_img(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

def main():
   html = get_html("http://tieba.baidu.com/p/2460150866")
   imglist =get_img(html)
   print imglist
   x = 0
   for imgurl in imglist:
       urllib.urlretrieve(imgurl, 'Img/%s.jpg' % x)
       x += 1


if __name__ == '__main__':
    main()

