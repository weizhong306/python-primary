# 網路連線
import urllib.request as request
# src = "http://www.ntu.edu.tw/"  # 台灣大學網站網址 
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")  # 取得台灣大學網站的原始碼(HTML、CSS、JS)
# print(data)


# 串接、擷取公開資料
import json
src = "https://ws.yunlin.gov.tw/001/Upload/539/opendata/15369/1698/6b05c6b0-899c-4eec-b01d-4ad3b6d3e518.json"  # 台灣大學網站網址 
with request.urlopen(src) as response:
    data = json.load(response)  # 利用json模組處理json資料格式
# print(data)

# 取得【ICD-10國際死因分類號碼】，列表出來
dlist = data
# print(dlist)
with open("data.txt", "w", encoding="utf-8") as file:
    for dname in dlist:
        # print(dname["ICD-10國際死因分類號碼"])
        file.write(dname["ICD-10國際死因分類號碼"]+"\n")
