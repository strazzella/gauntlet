SETUP:
-Type: mkdir projects
-Type: mkdir gauntlet
-Install necessary tech: python3, pip, etc.
-Create a virtual env using the following command: python3 -m venv ./venv
-Activate env by using this command in project folder after created env: source venv/bin/activate
-Install django: python3 -m pip install django
-Start project: django-admin startproject *name of app* .
-*OPTIONAL* Start collection: django-admin startapp collection

NOTES:
-For paths it is django.urls import path NOT django.conf.urls import path
-URL Patters use path() not url(). If you still wish to use regex url, use re_path(). Make sure to import re_path
-In templates, use {% load static %} now, NOT {% load staticfiles %}
