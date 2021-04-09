#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('spirited_away/<int:comment_id>', views.spirited_away_comments, name='spirited_away_comments'),
    path('spirited_away/index', views.spirited_away_index, name='spirited_away_index'),
    path('NeZha/index', views.nezha_index, name='nezha_index'),
    path('NeZha/<int:comment_id>', views.nezha_comments, name='nezha_comments'),
]