# 數字運算
x1 = 3 + 6
print(x1)
x2 = 3 - 6
print(x2)
x3 = 3 * 6
print(x3)
x4 = 7 / 6  # 小數除法
print(x4)
x5 = 3 ** 6  # 3的6次方
print(x5)
x6 = 7 // 6  # 整數除法
print(x6)
x7 = 7 % 6  # 取餘數
print(x7)

x8 = 2 + 3
x8 += 1  # x8 = x8 + 1 # 將變數中的數字 +1 其他運算以此類推
print(x8)

# 字串運算
# 字串會對內部的字元編號(索引)，從0開始算起
s1 = "Hello"  # s = 'HEllo"
print("s1: " + s1)
s2 = "Hell\"o"  # \ 跳脫符號原先特別的功能
print("s2: " + s2)
s3 = "Hello\nWorld"  # \n 換行 Python中 """ ''' 也是換行
print("s3: " + s3)
s4 = """Hello


World"""
print("s4: " + s4)
s5 = "Hello" * 3
print("s5: " + s5)
s6 = "Hello"
print("s6: " + s6[1:4])
print("s6: " + s6[1:])
print("s6: " + s6[:4])
