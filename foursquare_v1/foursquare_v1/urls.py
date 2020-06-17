from django.urls import path,include

urlpatterns = [
    #path('admin/',include('main.urls')),
    path('api/v1/', include('main.api_v1.urls')),
]
