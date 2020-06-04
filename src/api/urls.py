from django.urls import path, include
from rest_framework import routers
from .views import (
    CADRecordList,
    CADRecordDetail
)


api_urls = [
    path('snippets/', CADRecordList),
    path('snippets/<int:pk>/', CADRecordDetail),
]

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('v1/', include(api_urls))
]