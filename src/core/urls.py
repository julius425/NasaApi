from django.urls import path
from .views import (
    Index,
    EndpointRequestView
)

"""
TODO: EndpointRequestView data processing urls (form, etc)
"""

urlpatterns = [
    path('', Index.as_view, name='index'),
    path('<slug>', EndpointRequestView.as_view, name='page_detail')
]