# 隨機選取

import random

# data = random.choice([1, 5, 6, 10, 20])
# print(data)

# data = random.sample([1, 5, 6, 10, 20], 3)
# print(data)


# 隨機調換順序(洗牌的概念)

# data = [1, 5, 8, 20]
# random.shuffle(data)
# print(data)


# 隨機取得亂數

# data = random.random()  # 0~1之間的隨機亂數
# print(data)
# data = random.uniform(60, 100)  # 60~100之間的隨機亂數 
# print(data) 


# 取得常態分配亂數

# 平均數100，標準差10，取得的資料【多數】在 90~110之間
# data = random.normalvariate(100, 10)
# print(data)

# 平均數0，標準差5，取得的資料【多數】在 -5~5之間
# data = random.normalvariate(0, 5)
# print(data)


# 統計模組

import statistics as stat
# 平均數
data = stat.mean([1, 4, 5, 8])
print(data)
# 中位數(去除極端值)
data = stat.median([1, 2, 3, 4, 5, 8, 1000])
print(data)
# 標準差(資料的散佈狀況)
data = stat.stdev([1, 2, 3, 4, 5, 8, 100])
print(data)
data = stat.stdev([1, 2, 3, 4, 5, 8, 10])
print(data)


