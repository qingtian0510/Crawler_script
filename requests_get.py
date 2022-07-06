import requests
query = input("请输入关键词：\n")
url = f'https://www.sogou.com/web?query={query}'

header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}

resp = requests.get(url, headers=header)
print(resp)
print(resp.text)

resp.close()
