# 抓取Medium.com的文章資料

import json
import urllib.request as req

url = "https://medium.com/_/api/home-feed"
# 建立一個Request物件，附加Request Headers的資訊(讓程式連線像個普通的使用者)
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  # 根據觀察，取得的資料是JSON格式


# 解析JSON格式的資料，取得每篇文章的標題

data = data.replace("])}while(1);</x>", "")  # 將JSON檔中影響讀取的部分去除
data = json.loads(data)  # 把原始的JSON資料解析成字典/列表的表示形式
print(data)

# 取得 JSON 資料中的文章標題

posts = data["payload"]["references"]["Post"]
for key in posts:
    post = posts[key]
    print(post["title"])
