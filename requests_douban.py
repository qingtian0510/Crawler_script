import requests

url = "https://movie.douban.com/j/new_search_subjects"

param = {
    "sort": "U",
    "range": "0,10",
    "tags": "",
    "start": "0"
}


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}

resp = requests.get(url=url, params=param, headers=headers)
print(resp.request.url)
print(resp.json())

resp.close()