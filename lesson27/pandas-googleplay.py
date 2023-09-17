import pandas as pd
# 讀取資料
data = pd.read_csv("googleplaystore.csv")  # 會將 csv 格式的檔案讀取成一個 DataFrame
# 觀察資料
print("資料數量", data.shape)
print("資料欄位", data.columns)
print("----------------------------")

# 分析資料：評分的各種統計數據
# condition = data["Rating"] <= 5  # 排除錯誤的資料(評分不應超過5分)
# data = data[condition]
# print("平均數", data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("取得前一千名位應用程式的平均評分", data["Rating"].nlargest(1000).mean())

# 分析資料：安裝數量的各種統計數據
# # 將原先字串型態的資料改為浮點數型態，在轉換過程中先將字串裡的, + Free清除掉
# data["Installs"] = pd.to_numeric(
#     data["Installs"].str.replace("[,+]", "", regex=True).replace("Free", ""))
# print("平均數", data["Installs"].mean())
# condition = data["Installs"] > 100000
# print("安裝數量大於10萬的應用程式有幾個", data[condition].shape[0])

# 基於資料的應用：關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字：")
condition = data["App"].str.contains(keyword, case=False)  # case=False忽略大小寫
print("包含關鍵字的應用程式數量", data[condition].shape[0])
