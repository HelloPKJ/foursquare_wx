import json

from django.http import JsonResponse
from main.api_v1.servers.get import view as view_of_get
from main.api_v1.servers.get import config as config_of_get
from main.api_v1.servers.post import view as view_of_post
from django.views.decorators.csrf import csrf_exempt


# 获取所有客户信息
def customers_all(request):
    state = {
        "code" : "",
        "error" : "",
        "msg":"",
        "data":{}
    }

    if request.method == 'GET':
        customers_list, error = view_of_get.get_random_customers_list(config_of_get.CUSTOMERS_LIST_SIZE)
        if error == None:
            state["code"] = "200"
            state["error"] = error
            state["msg"] = "success"
            state["data"] = customers_list
        else:
            state["code"] = "100000"
            state["error"] = error
            state["msg"] = "fail"
            state["data"] = customers_list

    return JsonResponse(state)

def customers_optional(request):
    state = {
        "code": "",
        "error": "",
        "msg": "",
        "data": {}
    }
    data_sources_id = request.GET.get("data_sources_id")
    trades_id = request.GET.get("trades_id")
    country_name = request.GET.get("country_name")
    customers_list,error = view_of_get.get_optional_customers_list(config_of_get.CUSTOMERS_LIST_SIZE,
                                                             data_sources_id,
                                                             trades_id,country_name)
    if error == None:
        state["code"] = "200"
        state["error"] = error
        state["msg"] = "success"
        state["data"] = customers_list
        return JsonResponse(state)
    else:
        state["code"] = "101000"
        state["error"] = error
        state["msg"] = "fail"
        state["data"] = customers_list
        return JsonResponse(state)

def init_base_data(request):
    state = {
        "code": "",
        "error": "",
        "msg": "",
        "data": {}
    }
    init_base_data_list,error = view_of_get.init_base_data()
    if error == None:
        state["code"] = "200"
        state["error"] = error
        state["msg"] = "success"
        state["data"] = init_base_data_list
        return JsonResponse(state)
    else:
        state["code"] = "109000"
        state["error"] = error
        state["msg"] = "fail"
        state["data"] = init_base_data_list
        return JsonResponse(state)

@csrf_exempt
def wx_login(request):
    state = {
        "code": 0,
        "error": "",
        "msg": "",
        "data": {}
    }
    js_code = json.loads(request.body.decode("utf-8"))["js_code"]
    print(js_code)
    token = view_of_post.wx_login(js_code)
    state["data"]["token"] = token
    return JsonResponse(state)

@csrf_exempt
def wx_login_auth(request):
    state = {
        "code": 0,
        "error": "",
        "msg": "",
        "data": {}
    }
    wx_token = json.loads(request.body.decode("utf-8"))["token"]
    print(wx_token)
    res = view_of_post.check_token(wx_token)
    state["data"]["has_login"] = res
    return JsonResponse(state)