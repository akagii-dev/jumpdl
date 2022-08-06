import urllib.request, time, os

def urasanday(urasundayIn):
    url = "https://urasunday.com/title/" + urasundayIn + ".html"
    urllib.request.urlretrieve(url, "./temp/manga.txt")
    f = open("./temp/manga.txt", "r", encoding="utf-8")
    pageList = []
    rmList = ['<meta property="og:title" content="', '" />', '｜裏サンデー', ' ', '\n']
    cnt = 0
    for line in f:
        if "src: " in line:
            line = line.replace("src: ", "").replace(",", "").replace("'", "")
            pageList.append(line)
            cnt += 1
        if '<meta property="og:title" content' in line:
            for i in rmList:
                line = line.replace(i, "")
            titleName = line
    f.close()
    os.mkdir("./output/" + titleName)
    for i in range(cnt):
        urllib.request.urlretrieve(pageList[i], "./output/"+titleName+"/"+str(i+1)+".png")
        time.sleep(0.1)
    os.remove("./temp/manga.txt")