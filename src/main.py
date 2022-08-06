import getJson, siteSlc, trimSize, urasunday, trim, os

try:
    os.mkdir("./output")
    os.makedirs("./temp/split")
except FileExistsError:
    pass

url = siteSlc.siteSlc()
mangaName = siteSlc.getMangaName()
if mangaName !="裏サンデー":
    print("task is running")
    pageH = getJson.getURL(url, mangaName)[2]
    pageW = getJson.getURL(url, mangaName)[3]
    titleName = getJson.getURL(url, mangaName)[4]
    trimH = trimSize.getTrimSize(mangaName, pageW)[0]
    trimW = trimSize.getTrimSize(mangaName, pageW)[1]
    os.mkdir("./output/" + titleName)
    trim.trim(mangaName, pageW, pageH, trimW, trimH, url, titleName)
    print("downloaded succeccfully")
elif mangaName == "裏サンデー":
    urasundayIn = input("Input title id/epsode id:")
    print("task is running")
    urasunday.urasanday(urasundayIn)
    print("downloaded succeccfully")