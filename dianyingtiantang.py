import requests
import re

domain = "https://dytt89.com/"
resp = requests.get(domain, verify=False)  #verify=False 去掉安全验证
resp.encoding = 'gb2312'  #指定编码方式

print(resp.text)