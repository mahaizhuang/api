# /bin/python
import requests
import json
import os 
import sys
import math
import time
import sys
#
class ssh1(object):
        def __init__(self):
            self.out = "json"
            self.time1 = time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime())
        def run_dujitang(self):
            dujitangurl = "https://v.api.aa1.cn/api/api-wenan-dujitang/index.php"
            params1={
		    'aa1':'json'
            }
            result1= requests.get(dujitangurl,params1)
            result1 = result1.json()
            result1 = ((result1[0])['dujitang'])
            print (self.time1,result1)  
            #
            path1 = os.path.abspath(os.path.dirname(__file__))
            path1 = os.path.join(path1,'毒鸡汤')
            if not os.path.exists(path1):
                os.mkdir(path1)
            #
            strdir1 = os.path.join(path1,'毒鸡汤.txt')
            with open (strdir1,'a+',encoding='utf-8') as f:
                f.write(self.time1 + "  " + result1 + '\r')
            f.close() 
        def run_muxiuge(self):
            muxiugeurl = "http://api.muxiuge.cn/API/tiangou.php"
            params1={}
            result1= requests.get(muxiugeurl,params1)
            result1 = result1.json()
            result1 = result1['text']
            #
            path1 = os.path.abspath(os.path.dirname(__file__))
            path1 = os.path.join(path1,'舔狗语录')
            if not os.path.exists(path1):
                os.mkdir(path1)
            #
            strdir1 = os.path.join(path1,'舔狗语录.txt')
            with open (strdir1,'a+',encoding='utf-8') as f:
                f.write(self.time1 + "  " + result1 + '\r')
            f.close()             
            print (self.time1,result1) 
        def run_king(self):
            kingurl = "http://api.muxiuge.cn/API/tiangou.php"
            params1={}
            result1= requests.get(kingurl,params1)
            result1 = result1.json()
            print (result1)

if __name__ == '__main__':
    a=ssh1()
    #a.run_dujitang()    
    #a.run_muxiuge() 
       
#

