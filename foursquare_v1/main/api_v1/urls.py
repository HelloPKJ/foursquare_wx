from django.urls import path
from main.api_v1 import views

urlpatterns = [
    # 获取所有客户信息
    path('customers/all/', views.customers_all),

    # 可选性的获取客户信息
    path('customers/optional',views.customers_optional),

    # 初始化一些基础数据
    path('init_base_data/',views.init_base_data),

    # 微信登陆
    path('wx_login/',views.wx_login),

    # 微信是否登陆了的校验
    path('wx_login_auth/',views.wx_login_auth),
]