# -*- coding: UTF-8 -*-
import shutil

import requests, json
from Crypto.Cipher import AES
import base64
import xlwt
import os
from model.applicationDB import getApplicationByOpenID, getAllApplication

# 如果text不足16位的倍数就用空格补足为16位
from server.adminServer import application2pdf


def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))
        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')
        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]


# 加密函数
def encrypt(data):
    key = '9999999999999999'
    vi = '0102030405060708'
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 加密后得到的是bytes类型的数据
    encodestrs = base64.b64encode(encryptedbytes)
    # 使用Base64进行编码,返回byte字符串
    enctext = encodestrs.decode('utf8')
    # 对byte字符串按utf-8进行解码
    return enctext


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(data):
    key = '9999999999999999'
    vi = '0102030405060708'
    data = data.encode('utf8')
    encodebytes = base64.decodebytes(data)
    # 将加密数据转换位bytes类型数据
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    unpad = lambda s: s[0:-s[-1]]
    text_decrypted = unpad(text_decrypted)
    # 去补位
    text_decrypted = text_decrypted.decode('utf8')
    return text_decrypted


def onLogin(code, encryptedData, iv):
    """LOGIN处理函数"""
    appID = 'wxcc21efcb27bb9083'  # 开发者关于微信小程序的appID
    appSecret = 'e36c790f3bb0c1828cc7487d4ae8dda9'  # 开发者关于微信小程序的appSecret
    req_params = {
        'appid': appID,
        'secret': appSecret,
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    wx_login_api = 'https://api.weixin.qq.com/sns/jscode2session'
    response_data = requests.get(wx_login_api, params=req_params)  # 向API发起GET请求
    resdata = response_data.json()
    openid = resdata['openid']  # 得到用户关于当前小程序的OpenID
    session_key = resdata['session_key']  # 得到用户关于当前小程序的会话密钥session_key
    print(session_key, openid)
    pc = WXBizDataCrypt(appID, session_key)  # 对用户信息进行解密
    userInfo = pc.decrypt(encryptedData, iv)  # 获得用户信息
    print(userInfo)
    user = getApplicationByOpenID(userInfo['openId'])
    if (user):
        return {"enOpenID": encrypt(userInfo['openId']), "exist": 1}
    else:
        return {"enOpenID": encrypt(userInfo['openId']), "exist": 0}


# TODO  实现用户验证
def checkUser(session_id):
    return True


# TODO 图片获取
def getExcel(applications):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    row = 0
    titles = ["姓名", "学号", "原学院", "原专业", "身份证号", "手机号", "绩点", "年级", "是否同意降级", "是否读博", "毕业后选择", "四级成绩", "六级成绩"]
    l = 0
    for title in titles:
        ws.write(row, l, title)
        l = l + 1
    row = row + 1
    for application in applications:
        if (application.CET == 0):
            CET = "四级"
        else:
            CET = "六级"
        D = ""
        if (application.doctor == 0):
            D = "否"
        else:
            D = "是"
        Downgrad = ""
        if application.downGrade == 0:
            Downgrad = "否"
        else:
            Downgrad = "是"
        c = ""
        if application.choiceAfterGraduating == 0:
            c = "国外深造"
        elif application.choiceAfterGraduating == 1:
            c = "国内读研"
        elif application.choiceAfterGraduating == 2:
            c = "就业"
        else:
            c = "待定"
        ws.write(row, 0, application.name)
        ws.write(row, 1, application.studentID)
        ws.write(row, 2, application.institute)
        ws.write(row, 3, application.major)
        ws.write(row, 4, application.ID)
        ws.write(row, 5, application.phoneNumber)
        ws.write(row, 6, application.GPA)
        ws.write(row, 7, application.grade)
        ws.write(row, 8, Downgrad)
        ws.write(row, 9, D)
        ws.write(row, 10, c)
        if application.CET == 1:
            ws.write(row, 11, "未提交")
            ws.write(row, 12, application.CETScore)
        else:
            ws.write(row, 12, "未提交")
            ws.write(row, 11, application.CETScore)

        row = row + 1
    wb.save("export/applications.xls")


def outputdir():
    if os.path.exists(r'export') is not True:
        os.mkdir('export')
    else:
        del_file('export')
    applications = getAllApplication()
    getExcel(applications)
    for application in applications:
        dirpath = "export/" + application.studentID
        if os.path.exists(dirpath) is not True:
            os.mkdir(dirpath)
        application2pdf(application, dirpath + "/")
        shutil.copy(application.CETRecord, dirpath + "/CETRecord." + getPictype(application.CETRecord))
        shutil.copy(application.academicRecord,
                    dirpath + "/academicRecord." + getPictype(application.academicRecord))
        num = 1
        for i in application.specialities:
            shutil.copy(i, dirpath + "/specialities" + str(num) + "." + getPictype(i))
            num = num + 1
        num = 1
        for i in application.otherFiles:
            shutil.copy(i, dirpath + "/otherFiles" + str(num) + "." + getPictype(i))
            num = num + 1
    shutil.make_archive("out", "zip", "export")


def getPictype(path):
    l = path.split(".")
    return l[-1]

def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def setExcel(applications):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    row = 0
    titles = ["姓名", "学号", "原学院", "原专业", "身份证号", "手机号", "绩点",
              "年级", "是否同意降级", "是否读博", "毕业后选择", "四级成绩", "六级成绩"]
    l = 0
    for title in titles:
        ws.write(row, l, title)
        l = l + 1
    row = row + 1
    for application in applications:
        ws.write(row, 0, application.name)
        ws.write(row, 1, application.studentID)
        ws.write(row, 2, application.institute)
        ws.write(row, 3, application.major)
        ws.write(row, 4, application.ID)
        ws.write(row, 5, application.phoneNumber)
        ws.write(row, 6, application.GPA)
        ws.write(row, 7, application.grade)
        row = row + 1
    wb.save("export/applications.xls")
