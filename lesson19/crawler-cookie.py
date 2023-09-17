# 抓取PTT八卦版的網頁原始碼(HTML)
import bs4
import urllib.request as req


def getData(url):
    # 建立一個Request物件，附加Request Headers的資訊(讓程式連線像個普通的使用者)
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)

    # 解析原始碼，取得每篇文章的標題

    # 運用 BrautifulSoup 協助我們解析 HTML 格式文件
    root = bs4.BeautifulSoup(data, "html.parser")
    # print(root.title.string) # 網頁標籤中的文字

    titles = root.find_all("div", class_="title")  # 尋找【所有】class="title"的div標籤
    # print(titles)

    for title in titles:
        if title.a is not None:  # 如果標題包含a標籤(沒有被刪除)，印出來
            print(title.a.string)

    # 抓取上一頁的連結
    nextLink = root.find("a", string="‹ 上頁")  # 找到內文是 ‹ 上頁 的a標籤
    return (nextLink["href"])


# 主程序：抓取多個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 5:  # 抓5頁
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1
    # print(pageURL)
