import urllib.request, json

def getURL(url, mangaName):
    urllib.request.urlretrieve(url, "./temp/manga.json")
    jsonOpen = open("./temp/manga.json", "r", encoding="utf-8")
    jsonData = json.load(jsonOpen)
    flag = True
    cnt = 0
    pageList = []
    pageH = jsonData["readableProduct"]["pageStructure"]["pages"][5]["height"]
    pageW = jsonData["readableProduct"]["pageStructure"]["pages"][5]["width"]
    titleName = jsonData["readableProduct"]["title"]
    while flag:
        try:
            pageList.append(jsonData["readableProduct"]["pageStructure"]["pages"][cnt]["src"])
            cnt+=1
        except KeyError:
            cnt +=1
        except IndexError:
            break
    if mangaName != "サンデーうぇぶり":
        return pageList, cnt-5, pageH, pageW, titleName
    else:
        return pageList, cnt, pageH, pageW, titleName