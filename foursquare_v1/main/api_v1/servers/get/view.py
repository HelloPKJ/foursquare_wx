import random

from main.public import models
from main.public import utils
from django.db.models import Q
from main.api_v1.servers.get import config


# 函数编号：100000
# 从随机获取数据库客户并封装为列表
def get_random_customers_list(customers_list_size):
    """
    :param customers_list_size: 一次需要获取多少个客户信息
    :return: 返回一个存放客户信息的列表，每个列表元素都是一个客户信息对象
    """
    # 1、从获取客户信息，转化为列表类型
    # 2、把客户信息里面的数据来源ID和所属行业ID转化为对应的中文
    error = None
    try:
        customers_list = get_data_sources_name(get_trades_name(list(models.CustomerTable.objects.values())))
    except:
        customers_list = []
        error = "服务器发送错误，错误代码：100001"
        return customers_list,error
    else:
        # 1、获取客户信息的长度
        # 2、如果长度小于配置设置的长度，则直接使用实际获取得到的数据长度
        customers_count = customers_list.__len__()
        if customers_count < customers_list_size:
            customers_list_size = customers_count

        # 从最终的客户信息列表中，随机抽取customers_list_size个客户信息
        customers_list = random.sample(customers_list, customers_list_size)
        return customers_list,error


# 函数编码：108000
# 把客户信息列表里面的所属行业ID转换为所属行业表中对应的中文名称
def get_trades_name(customers_list):
    trades_list = list(models.TradesTable.objects.values("trades_id", "trades_name_cn"))
    for customer in customers_list:
        for trade in trades_list:
            if customer["customer_trades_id"] == trade["trades_id"]:
                customer["customer_trades_id"] = trade["trades_name_cn"]
    return customers_list


# 把客户列表里面的数据来源ID转换为数据来源表中对应的名称
def get_data_sources_name(customers_list):
    data_sources_list = list(models.DataSourcesTable.objects.values("data_sources_id", "data_sources_name_cn"))
    for customer in customers_list:
        for data_sources in data_sources_list:
            if customer["customer_data_sources_id"] == data_sources["data_sources_id"]:
                customer["customer_data_sources_id"] = data_sources["data_sources_name_cn"]
    return customers_list


# 函数编号：101000
# 可选的性的从客户信息表中随机获取指定个数的客户信息
def get_optional_customers_list(customers_list_size,data_sources_id,trades_id,country_name):
    """
    :param customers_list_size: 一次需要获取多少个客户信息
    :param data_sources_id: 数据来源ID
    :param trades_id: 所属行业ID
    :param country_name: 国籍中文名称
    :return: 返回一个存放客户信息的列表，每个列表元素都是一个客户信息对象
    """
    error = None
    q = Q()
    q.connector = "and"

    # 1、判断数据来源ID是否为0，为0零表示选择了"全部"，则直接pass，不成为筛选条件
    # 2、如果不为0，则列为筛选条件，并判断该数据来源ID是否为合法，比如是否存在恶意攻击代码
    if data_sources_id == "0":
        pass
    elif is_true_data_sources_id(data_sources_id) == True:
        q.children.append(("customer_data_sources_id", data_sources_id))
    else:
        error = "找不到相应的数据"

    # 1、判断所属行业ID是否为0，为0零表示选择了"全部"，则直接pass，不成为筛选条件
    # 2、如果不为0，则列为筛选条件，并判断该所属行业ID是否为合法，比如是否存在恶意攻击代码
    if trades_id == "0":
        pass
    elif is_true_trades_id(trades_id) == True:
        q.children.append(("customer_trades_id", trades_id))
    else:
        error = "找不到相应的数据"

    # 1、判断国籍名称是否为"全部"
    # 2、如果不为"全部"，则列为筛选条件，并判断该国籍名称是否为合法，比如是否存在恶意攻击代码
    if country_name == "全部":
        pass
    elif is_true_country(country_name) == True:
        q.children.append(("customer_region2_cn", country_name))
    else:
        error = "找不到相应的数据，或者检查国籍是否输入有误"

    # 1、如果上面的数据来源、所属行业、国籍名称均为"全部"，则直接从客户信息列表中随机获取指定个数的客户信息即可
    # 2、否则把上面筛选过的搜索条件封装为Q对象，从对应数据库中获取客户数据
    if data_sources_id == "0" and trades_id == "0" and country_name == "全部" :
        customers_list,error = get_random_customers_list(config.CUSTOMERS_LIST_SIZE)
        return customers_list,error
    else:
        try:
            customers_list = get_data_sources_name(get_trades_name(list(models.CustomerTable.objects.values().filter(q))))
        except:
            customers_list = []
            error = "服务器发生错误，错误代码：101001"
            return customers_list, error
        else:
            customers_count = customers_list.__len__()
            if customers_count < customers_list_size:
                 customers_list_size = customers_count
            print("类型",type(customers_list))
            print("类型值", customers_list)
            customers_list = random.sample(customers_list, customers_list_size)
            return customers_list,error


# 函数编号：102000
# 获取数据来源表的全部数据
def get_data_source_list():
    error=None
    try:
        data_source_list = list(models.DataSourcesTable.objects.values("data_sources_id","data_sources_name_cn"))
    except:
        data_source_list = []
        error = "服务器发生错误，错误代码：102001"
        return data_source_list, error
    else:
        return data_source_list,error


# 函数编码：103000
# 获取所属行业的全部数据
def get_trades_list():
    error = None
    try:
        trades_list = list(models.TradesTable.objects.values("trades_id", "trades_name_cn"))
    except:
        trades_list = []
        error = "服务器发生错误，错误代码：103001"
        return trades_list, error
    else:
        return trades_list,error


# 函数编码：104000
# 获取热门国家表的全部数据
def get_hot_country_list():
    error = None
    try:
        hot_country_list = list(models.HotCountryTable.objects.values("hot_country_id","hot_country_cn"))
    except:
        hot_country_list = []
        error = "服务器发生错误，错误代码：104001"
        return hot_country_list,error
    else:
        return hot_country_list, error

# 函数编码：105000
# 获取评价表的全部数据
def get_evaluation_list():
    error = None
    try:
        evaluation_list = list(models.EvaluationTable.objects.values("evaluation_id","evaluation_img","evaluation_title",
                                                                "evaluation_content"))
    except:
        evaluation_list = []
        error = "服务器发生错误，错误代码：105001"
        return evaluation_list,error
    else:
        return evaluation_list, error

# 函数编码：106000
# 获取关于我们表的全部数据
def get_about_list():
    error = None
    try:
        about_list = list(models.AboutTable.objects.values("about_id","about_logo","about_explain","about_notice",
                                                            "about_website","about_Contact","about_qrcode_img",
                                                            "about_qrcode_explain"))
    except:
        about_list = []
        error = "服务器发生错误，错误代码：106001"
        return about_list,error
    else:
        return about_list,error

# 函数编码：107000
# 获取广告表的全部数据
def get_ad_list():
    error = None
    try:
        ad_list = list(models.AdsTable.objects.values("ads_id","ads_img","ads_url","ads_click_num"))
    except:
        ad_list = []
        error = "服务器发生错误，错误代码：107001"
        return ad_list,error
    else:
        return ad_list, error


# 函数编码：109000
# 封装一些基础数据，比如所属行业、数据来源、热门国家、广告图片等
# 一次性请求响应，可以减轻服务器处理压力
def init_base_data():
    error = None
    init_base_data_list = []

    data_source_list,error = get_data_source_list()
    if error == None:
        init_base_data_list.append(data_source_list)
    else:
        init_base_data_list = []
        error = "服务器发生错误，错误代码：" + str(error)
        return init_base_data_list,error

    trades_list, error = get_trades_list()
    if error == None:
        init_base_data_list.append(trades_list)
    else:
        init_base_data_list = []
        error = "服务器发生错误，错误代码：" + str(error)
        return init_base_data_list, error

    hot_country_list, error = get_hot_country_list()
    if error == None:
        init_base_data_list.append(hot_country_list)
    else:
        init_base_data_list = []
        error = "服务器发生错误，错误代码：" + str(error)
        return init_base_data_list, error

    evaluation_list, error = get_evaluation_list()
    if error == None:
        init_base_data_list.append(evaluation_list)
    else:
        init_base_data_list = []
        error = "服务器发生错误，错误代码：" + str(error)
        return init_base_data_list, error

    about_list, error = get_about_list()
    if error == None:
        init_base_data_list.append(about_list)
    else:
        init_base_data_list = []
        error = "服务器发生错误，错误代码：" + str(error)
        return init_base_data_list, error

    ad_list, error = get_ad_list()
    if error == None:
        init_base_data_list.append(ad_list)
    else:
        init_base_data_list = []
        error = "服务器发生错误，错误代码：" + str(error)
        return init_base_data_list, error

    return init_base_data_list,error


# 判断国籍名称是否合法
def is_true_country(country_name):

    # 判断输入的是否为空
    if country_name.isspace():
        return False

    # 判断用户输入的国家名称是否合法性，判断是否存在恶意攻击的关键字等
    if utils.is_bad_str(country_name):
        true_country_name = utils.strip_all(country_name)
        res = models.CustomerTable.objects.values("customer_region2_cn").filter(customer_region2_cn = true_country_name)
        if res.count() == 0:
            return False
        else:
            return True


# 判断数据来源ID是否合法
def is_true_data_sources_id(data_sources_id):

    # 判断输入的是否为空
    if data_sources_id.isspace():
        return False

    # 判断数据来源ID是否合法性，判断是否存在恶意攻击的关键字等
    if utils.is_bad_str(data_sources_id):
        res = models.CustomerTable.objects.values("customer_id").filter(customer_data_sources_id = data_sources_id)
        if res.count() == 0:
            return False
        else:
            return True

# 判断数据来源ID是否合法
def is_true_trades_id(trades_id):

    # 判断输入的是否为空
    if trades_id.isspace():
        return False

    # 判断数据来源ID是否合法性，判断是否存在恶意攻击的关键字等
    if utils.is_bad_str(trades_id):
        res = models.CustomerTable.objects.values("customer_id").filter(customer_trades_id = trades_id)
        if res.count() == 0:
            return False
        else:
            return True




