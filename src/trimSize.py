trimSizeList = [["少年ジャンプ＋", 1184, 800]
                ,["少年ジャンプ", 1184, 736]
                , ["サンデーうぇぶり", 2048, 1408]
                ,["サンデーうぇぶり", 2048, 1440]
                , ["となりのヤングジャンプ", 1120, 800]]

def getTrimSize(mangaName, pageW):
    if mangaName == "少年ジャンプ＋":
        if pageW == 822:
            return trimSizeList[0][1], trimSizeList[0][2]
        elif pageW == 764:
            return trimSizeList[1][1], trimSizeList[1][2]
    elif mangaName == "サンデーうぇぶり":
        if pageW == 1426:
            return trimSizeList[2][1], trimSizeList[2][2]
        elif pageW == 1445:
            return trimSizeList[3][1], trimSizeList[3][2]
    elif mangaName == "となりのヤングジャンプ":
        return trimSizeList[3][1], trimSizeList[3][2]
