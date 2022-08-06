trimSizeList = [["少年ジャンプ＋", 1184, 800]
                , ["サンデーうぇぶり", 2048, 1408]
                ,["サンデーうぇぶり", 2048, 1440]
                , ["となりのヤングジャンプ", 1120, 800]]

def getTrimSize(mangaName, pageW):
    if mangaName == "少年ジャンプ＋":
        return trimSizeList[0][1], trimSizeList[0][2]
    elif mangaName == "サンデーうぇぶり":
        if pageW == 1426:
            return trimSizeList[1][1], trimSizeList[1][2]
        elif pageW == 1445:
            return trimSizeList[2][1], trimSizeList[2][2]
    elif mangaName == "となりのヤングジャンプ":
        return trimSizeList[3][1], trimSizeList[3][2]