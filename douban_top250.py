import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}
resp = requests.get(url, headers=headers)
page_content = resp.text

# 解析数据
# re.S 保湿 . 可以匹配任意字符，包括换行
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
                 r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

# 开始匹配
result = obj.finditer(page_content)

f = open("data.csv", mode="w")
csvwriter = csv.writer(f)

for it in result:
    # print(it.group("name"))
    # print(it.group("year").strip())
    # print(it.group("score"))
    # print(it.group("num"))
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())

f.close()
print("over")