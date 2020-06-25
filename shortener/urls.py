from django.contrib import admin
from django.urls import path, include
from short.views import shortenerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shortenerView),
    path('<slug:slug>/', shortenerView),
]
