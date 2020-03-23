from django.contrib import admin
from django.urls import path, include
from . import views # 화면을 보여주도록 할 views파일을 import함

# 맵 관련 path
urlpatterns = [
    path('', views.test, name='test'),  # 기본 등록 화면
    path('map/', views.map, name='map'),  # 기본 등록 화면
    path('map/add', views.map_add, name='map_add'),  # 등록 post처리
    path('map/list_all', views.map_list_all, name='map_list_all'),  # 전체 목록
]
