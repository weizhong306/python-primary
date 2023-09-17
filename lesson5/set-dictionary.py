# 集合的運算
# s1 = {3, 4, 5}
# print(3 in s1)
# print(10 in s1)
# print(10 not in s1)

# s1 = {3, 4, 5}
# s2 = {4, 5, 6, 7}
# s3 = s1 & s2  # 交集：取兩個集合中，相同的資料
# print(s3)
# s4 = s1 | s2  # 聯集：取兩個集合中的所有資料，但不重複取
# print(s4)
# s5 = s1 - s2  # 差集：從 s1 中，減去和 s2 重疊的部分
# print(s5)
# s6 = s1 ^ s2  # 反交集：取兩集合中，不重疊的部分
# print(s6)

# s = set("Hello")  # set(字串):把字串中的字母拆解成集合(相同字母只會取一次)
# print(s)
# print("H" in s)
# print("a" in s)


# 字典的運算: Key-Value 配對
dic = {"apple": "蘋果", "bug": "蟲"}

# print(dic["apple"])
# dic["apple"] = "小蘋果"
# print(dic["apple"])

# print("apple" in dic)  # 判斷 key 是否存在 dic 字典中
# print("test" in dic)
# print("test" not in dic)

# print(dic)
# del dic["apple"]  # 刪除字典中的鍵值對(key-value pair)
# print(dic)

# dic = {x: x*2 for x in 列表[]}
dic = {x: x*2 for x in [3, 4, 5]}  # 以列表的資料為基礎產生字典
print(dic)
