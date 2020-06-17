import json
import hashlib
from main.public import config

def to_list(queryset_data):
    """
    简介：传入queryset对象，转化为列表
    :param queryset_data: 【queryset类型对象】通过django orm从数据查询得到的数据集
    :return:
    """
    return list(queryset_data.values())

#本地不做保存
#生成token
def get_token(salt, openid):
    md5 = hashlib.md5()
    md5.update(salt.encode("utf-8"))
    md5.update(openid.encode("utf-8"))
    md5.update(salt.encode("utf-8"))
    return md5.hexdigest()

# 判断是否包含违法关键词
def is_bad_str(s):
    with open(config.BAN_STR_FILE_URL, 'r') as f:
        ban_str_list = f.readlines()
    for ban_str in ban_str_list:
        if ban_str == "" or " " or "\n" or "\r" or "\t":
            continue
        if strip_all(ban_str).lower() in strip_all(str(s)).lower():
            print(strip_all(ban_str).lower())
            print(strip_all(s).lower())
            # 包含不合法的关键字
            #print("不合法")
            return False

    # 筛选不出就表示合法
    #print("合法")
    return True

# 去除两端空格和右边的换行和回车
def strip_all(str):
    return str.strip().replace("\n","").replace("\r","")


