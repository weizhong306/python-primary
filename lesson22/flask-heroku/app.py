# 目前Heroku不再免，可以改用pythonanywhere  2023.9.15
from flask import Flask

app = Flask(__name__)  # __name__ 代表目前執行的模組


@app.route("/")  # 函式的裝飾(Decorator):以函式為基礎，提供附加功能
def home():
    return "Hello Flask"


@app.route("/test")  # 代表我們要處理的網路路徑
def test():
    return "This is Test"


if __name__ == "__main__":  # 如果以主程式執行
    app.run()  # 立刻啟動伺服器
