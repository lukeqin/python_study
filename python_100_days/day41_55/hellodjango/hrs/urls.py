#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/05/02 15:49
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : urls.py
# @notice ：


from django.urls import path

from hrs import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.show_subjects),
    path('teachers/', views.show_teachers),
    path('praise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('register/', views.register, name='register'),
    path('captcha/', views.get_captcha),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('excel/', views.export_teachers_excel),
    path('teachers_data/', views.get_teachers_data),
    path('echarts', views.echarts),
    path('show_subjects_json', views.show_subjects_json),
    path('show_subjects_json_bmpappers', views.show_subjects_json_bmpappers),
]