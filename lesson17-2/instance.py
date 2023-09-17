# Point 實體物件的設計：平面座標上的點

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # 定義實體方法
#     def show(self):
#         print(self.x, self.y)

#     def distance(self, targetX, targetY):
#         return (((self.x - targetX)**2) + ((self.y - targetY)**2))**0.5


# p = Point(3, 4)
# p.show()    # 呼叫實體方法／函式
# result = p.distance(0, 0)  # 計算座標(3, 4)和座標(0, 0)之間的距離
# print(result)


# File實體物件的設計：包裝檔案讀取的程式

class File:
    # 初始化函式
    def __init__(self, name):
        self.name = name
        self.file = None    # 尚未開啟檔案：初期是None

    def open(self):  # 自己定義的open實體方法
        self.file = open(self.name, mode="r",
                         encoding="utf-8")     # python內建的open

    def read(self):  # 自己定義的read實體方法
        return self.file.read()     # python內建的read


# 讀取第一個檔案
f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)

# 讀取第二個檔案
f2 = File("data2.txt")
f2.open()
data = f2.read()
print(data)
