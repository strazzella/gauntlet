from django.urls import include, path, re_path
from django.contrib import admin


urlpatterns = [
    path('gauntlet/accounts/', include('accounts.urls')),
    path('gauntlet/documents/', include('documents.urls')),
    path('gauntlet/admin/', admin.site.urls),
]
