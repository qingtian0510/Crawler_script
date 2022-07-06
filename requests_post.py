import requests

url = "https://fanyi.baidu.com/sug"

key = input("input: \n")

data = {
    "kw": key
}

resp = requests.post(url, data=data)

print(resp.json())  #将服务器返回的数据直接转成json -> dict
print(resp.close())