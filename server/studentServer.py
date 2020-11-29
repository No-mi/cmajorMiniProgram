import requests, json
from Crypto.Cipher import AES
import base64

from model.studentDB import getStudentUserByOpenId, insertStudent


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
    user = getStudentUserByOpenId(userInfo['openId'])
    if (user):
        print(user.to_json())
    else:
        insertStudent(userInfo['openId'], userInfo['nickName'], "123")
