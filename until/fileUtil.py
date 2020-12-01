# -*- coding: UTF-8 -*-
import base64
import os


def saveImg(img):
    print('saveImg')
    path = img['path']
    content = img['img']
    print('path', path)
    with open(path, 'wb') as file:
        img = base64.b64decode(content)
        print('imgcode', img)
        file.write(img)


def readImg(filePath):
    with open(filePath, "rb") as f:
        img = f.read()
    # 2、base64编码
    data = base64.b64encode(img).decode()

    # # 3、图片编码字符串拼接
    # src = "data:image/{ext};base64,{data}".format(ext=ext, data=data)
    return data
