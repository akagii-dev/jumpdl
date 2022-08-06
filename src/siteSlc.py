

managList = [["少年ジャンプ＋", "https://shonenjumpplus.com/episode/"]
            ,["サンデーうぇぶり", "https://www.sunday-webry.com/episode/"]
            ,["となりのヤングジャンプ", "https://tonarinoyj.jp/episode/"]
            ,["裏サンデー"]]

mangaName = []

def siteSlc():
    usrSlc = print("choose  manga site:")
    for i in range(len(managList)):
        print(str(i+1)+": "+managList[i][0])
    usrSlc = int(input(">>"))
    if usrSlc !=4:
        mangaID = input("Input episode id:")
        mangaName.append(managList[usrSlc-1][0])
        url = managList[usrSlc-1][1]+mangaID+".json"
        return url
    else:
        mangaName.append(managList[usrSlc-1][0])

def getMangaName():
    return mangaName[0]
