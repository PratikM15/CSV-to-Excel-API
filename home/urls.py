from django.urls import path, include
from . import views
urlpatterns = [
    path('api/convert', views.FileConvertView.as_view(), name="convert"),
]
