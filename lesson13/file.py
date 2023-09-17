# 儲存檔案

# # 開啟 # 開啟模式(w, r, r+) # 指定開啟編碼
# file = open("data.txt", mode="w", encoding="ut-8")
# file.write("Hello File\nSecond Line\n測試中文")  # 操作 # \n 換行
# file.close()  # 關閉

# 重複開啟寫入會覆蓋舊資料
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("Hello File\nSecond Line\n測試中文")


# 讀取檔案

# with open("data.txt", mode="r", encoding="utf-8") as file:
#     data = file.read()
# print(data)

# 把檔案中的數字資料，一行一行的讀出來，並計算總和
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("5\n3")
# sum = 0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for line in file:  # 一行一行的讀取
#         sum += int(line)
# print(sum)


# 使用 JSON 格式讀取、複寫檔案

import json 
# 從檔案中讀取JSON資料，放入變數data裡面
with open("config.json", mode="r") as file:
    data = json.load(file)
print(data) # data 是一個字典資料
print("name: ", data["name"]) # 注意取用字典資料的語法
print("version: ", data["version"])

data["name"] = "New Name" # 修改變數中的資料

# 把最新的資料複寫回檔案中
with open("config.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file)
