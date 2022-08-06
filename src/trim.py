import cv2, os, glob, getJson, urllib.request
from PIL import Image

def trim(mangaName, pageW, pageH, trimW, trimH, url, titleName):
    for i in range(getJson.getURL(url, mangaName)[1]):
        #置き換えない部分を先にトリミング
        try:
            urllib.request.urlretrieve(getJson.getURL(url, mangaName)[0][i], "./temp/"+str(i)+".png")
        except IndexError:
            break
        imgName =  "./temp/"+str(i)+".png"
        img = cv2.imread(imgName)
        if pageH != trimH and pageW != trimW:
            trimImg1 = img[0:trimH,trimW:pageW]
            cv2.imwrite("./temp/trim1.png", trimImg1)
            trimImg2 = img[trimH:pageH,0:pageW]
            cv2.imwrite("./temp/trim2.png", trimImg2)
            bfImg = img[0:trimH, 0:trimW]
        elif pageH == trimH:
            trimImg1 = img[0:pageH,trimW:pageW]
            cv2.imwrite("./temp/trim1.png", trimImg1)
            bfImg = img[0:pageH, 0:trimW]
        elif pageW == trimW:
            trimImg1 = img[trimH:pageH,0:pageW]
            cv2.imwrite("./temp/trim1.png", trimImg1)
            bfImg = img[0:trimH, 0:pageW]
        #置き換える(x, y座標をスワップ)
        h, w = bfImg.shape[:2]
        splitX, splitY = 4, 4
        chunksX, chunksY = 0, 0
        for j in range(splitX):
            for k in range(splitY):
                splitPic = bfImg[chunksY:chunksY+int(h/splitY), chunksX:chunksX+int(w/splitX)]
                cv2.imwrite('./temp/split/y'+str(j)+'x'+str(k)+'.jpg',splitPic)
                os.rename('./temp/split/y'+str(j)+'x'+str(k)+'.jpg','./temp/split/'+str(4*j+k)+'.jpg')
                chunksY+=int(h/splitY)
            chunksY=0
            chunksX+=int(w/splitX)
        combImgList = []
        for j in range(4):
            imgFh = cv2.hconcat([cv2.imread("./temp/split/"+str(4*j)+".jpg"),cv2.imread("./temp/split/"+str(4*j+1)+".jpg")])
            imgLh = cv2.hconcat([cv2.imread("./temp/split/"+str(4*j+2)+".jpg"),cv2.imread("./temp/split/"+str(4*j+3)+".jpg")])
            combImgList.append(cv2.hconcat([imgFh, imgLh]))

        #背景画像(白)に貼り付け
        afImg = cv2.vconcat([cv2.vconcat([combImgList[0], combImgList[1]]), cv2.vconcat([combImgList[2], combImgList[3]])])
        cv2.imwrite("./temp/afterImg.png", afImg)
        Image.new('RGB', (pageW, pageH), (255, 255, 255)).save("./temp/background.png")
        background = Image.open("./temp/background.png")
        afImg = Image.open("./temp/afterImg.png")
        background.paste(afImg, (0, 0))
        background.save("./temp/bgtemp1.png")
        background = Image.open("./temp/bgtemp1.png")
        trim1 = Image.open("./temp/trim1.png")
        if pageH != trimH and pageW != trimW:
            background.paste(trim1, (trimW, 0))
            background.save("./temp/bgtemp2.png")
            trim2 = Image.open("./temp/trim2.png")
            background.paste(trim2, (0, trimH))
            background.save("./output/"+titleName+"/"+str(i+1)+".png")
        elif pageH == trimH :
            background.paste(trim1, (trimW, 0))
            background.save("./output/"+titleName+"/"+str(i+1)+".png")
        elif pageW == trimW:
            background.paste(trim1, (0, trimH))
            background.save("./output/"+titleName+"/"+str(i+1)+".png")
        for j in range(16):
            os.remove("./temp/split/"+str(j)+".jpg")
        for name in glob.glob("./temp/*.png"):
            os.remove(name)
    os.remove("./temp/manga.json")