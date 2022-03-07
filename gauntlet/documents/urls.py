from django.urls import path, re_path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    re_path(r'^create/(?P<document_id>[0-9]+)$', views.create, name='create'),
    re_path(
        r'^delete/(?P<document_id>[\d]+)$',
        views.delete_doc,
        name='delete-doc'),
    path('create-new/', views.create_new, name='create-doc'),
    re_path(r'^(?P<document_id>[0-9]+)$', views.read, name='read'),
]
