import os
from os import listdir
import pickle as pickle
import numpy as np
from PIL import Image

data = {}
list1 = []
list2 = []
list3 = []

def img_tra():
    for k in range (0, num):
        currentPath = folder + "/" + imgList[k]
        im = Image.open(currentPath)
        x_s = 32
        y_s = 32
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        out.save(folder_ad + "/" + str(imgList[k]))

def addWord(theIndex, word, adder):
    theIndex.setdefault(word,[]).append(adder)

def seplabel(fname):
    filestr = fname.split(".")[0]
    label = int(filestr.split("_")[0])
    return label

def mkcf():
    global data
    global list1
    global list2
    global list3

    for k in range(0, num):
        currentPath = folder_ad + "/" + imgList[k]
        im = Image.open(currentPath)
        with  open(binpath, 'a') as f:
            for i in range(0,32):
                for j in range(0,32):
                    cl = im.getpixel((i,j))
                    list1.append(cl[0])
            for i in range(0,32):
                for j in range(0,32):
                    cl = im.getpixel((i,j))
                    list1.append(cl[1])
            for i in range(0,32):
                for j in range(0,32):
                    cl = im.getpixel((i,j))
                    list1.append(cl[2])
            list2.append(list1)
            list1 = []
            f.close()
            print("image" + str(k+1) + "saved")
            list3.append(imgList[k].encode('utf-8'))
        arr2 = np.array(list2, dtype=np.uint8)
        data['batch_label'.encode('utf-8')] = 'testing batch 1 of 1'.encode('utf-8')
        data.setdefault('labels'.encode('utf-8'),label)
    data.setdefault('data'.encode('utf-8'),arr2)
    data.setdefault('filenames'.encode('utf-8'),list3)
    output = open(binpath, 'wb')
    pickle.dump(data, output)
    output.close()

folder = "../image1"
folder_ad = "../image1"
imgList = listdir(folder_ad)
num = len(imgList)
label = []
for i in range(0,num):
    label.append(seplabel(imgList[i]))
    print(seplabel(imgList[i]))
binpath = "../image/test_batch"
mkcf()