# 載入pandas模組
import pandas as pd

# 建立Series
data = pd.Series([20, 10, 15])

# 基本Series操作
# print(data)
# print("Max", data.max())
# print("Median", data.median())
# data = data * 2
# data = data == 20
# print(data)

# 建立DataFrame
data = pd.DataFrame({
    "name": ["Amy", "John", "Bob"],
    "salary": [30000, 50000, 40000]
})
# print(data)

# 基本DataFrame操作
print(data)
print("-------------------")
# 取得特定的欄位
print(data["name"])
# 取得特定的列
print(data.iloc[0])  # 印出第一列
