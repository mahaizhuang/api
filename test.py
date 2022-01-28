# encoding: utf-8
# /bin/bash
import os
import json
import requests
#
def get_url(max_scrape_img_n,keyword,original_url):
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    sess=requests.Session()
    sess.headers['User-Agent'] = agent
    imgs_per_page = 30
    page_nos = max(1, max_scrape_img_n // imgs_per_page + 1)
    parameters = [{'tn': 'resultjson_com',
                   'ipn': 'rj',
                   'ct': 201326592,
                   'is': '',
                   'fp': 'result',
                   'fr': '',
                   'word': keyword,
                   'queryWord': keyword,
                   'cl': '',
                   'lm': '',
                   'ie': 'utf-8',
                   'oe': 'utf-8',
                   'adpicid': '',
                   'st': '',
                   'z': '',
                   'ic': '',
                   'hd': '',
                   'latest': '',
                   'copyright': '',
                   's': '',
                   'se': '',
                   'tab': '',
                   'width': '',
                   'height': '',
                   'face': '',
                   'istype': '',
                   'qc': '',
                   'nc': '',
                   'expermode': '',
                   'nojc': '',
                   'isAsync': '',
                   'pn': 30 * (page_no + 1),
                   'rn': 30,
                   'gsm': '5a',
                   '1642323736936': ''} for page_no in range(page_nos)]
    urls = []
    for param in parameters:
        data = sess.get(original_url, params=param).json().get('data')
        print (data)
    #    try:
    #        data = sess.get(original_url, params=param).json().get('data')
    #        img_urls = [d['thumbURL'] for d in data[:imgs_per_page]]
    #        urls.extend(img_urls)
    #    except json.decoder.JSONDecodeError:
    #        print("解析错误")
    #return urls
#
if __name__ == '__main__':
    url1=get_url(30,"杨超越","https://image.baidu.com/search/acjson")
    print (url1)
