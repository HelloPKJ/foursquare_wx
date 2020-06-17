import requests
import json

from public import config as public_config
from public import utils


# 微信登陆
def wx_login(js_code):

    # 整理请求微信登陆API的所属参数
    # appid：微信appid
    # secret：微信app密钥
    # js_code：微信前端调用wx-login得到的code
    # grant_type：微信login官方要求的固定必传参数，grant_type":"authorization_code
    wx_api_params = {"appid":public_config.APP_ID,
                     "secret":public_config.APP_SECRET,
                     "js_code":js_code,
                     "grant_type":"authorization_code"}

    # 向微信官方login接口发出请求获取openid和seesion_key
    # openid是微信当前用户唯一ID，类似身份证
    # seesion_key是微信返回的一个密钥，可以用判断当前在微信内部的登陆状态
    wx_response = requests.get(url = public_config.WX_API_URL, params = wx_api_params)
    res = json.loads(wx_response.content.decode("utf-8"))

    # 利用openid生成token
    token = utils.get_token(public_config.SALT, res["openid"]) + "|" + str(res["openid"])
    return token


# 校验token是否合法
def check_token(token):

    # 获取token部分
    from_wx_token = token.split("|")[0]

    # 获取openid部分
    from_wx_openid = token.split("|")[1]

    # 判断token是否一致
    true_token = utils.get_token(public_config.SALT, from_wx_openid)
    if from_wx_token == true_token:
        return True
    else:
        return False