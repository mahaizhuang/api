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
        def run_tuapi(self):
            hlapiurl = "https://tuapi.eees.cc/api.php"    #https://tuapi.eees.cc/
            params1={
                'type':self.out,
                'category':'meinv'
            }
            result1 = requests.get(hlapiurl,params1)
            result1 = result1.json()
            urldit = json.dumps(result1,indent=2)
            urldit = json.loads(urldit)
            url1 = urldit['img'] 
            print (url1)
            dowrul = requests.get(url1)
            #
            time2 = time.strftime("%Y%m%d-%H-%M-%S", time.localtime())
            path1 = "D:\\Tool\\vscode\\微编程\\py\\inter\\tuapi"
            folder = os.path.exists(path1)
            if not folder:
                os.makedirs(path1)
                print ("---  new folder...  ---\n---  OK  ---")
            else:
                print ("---  There is this folder!  ---")
            #
            imge1 =time2 + url1[-4:]
            vvhandir = os.path.join(path1,imge1)
            with open (vvhandir,"wb") as f:
                f.write(dowrul.content)
            f.close()
#
if __name__ == '__main__':
    a=ssh1()       
    a.run_tuapi()

#


