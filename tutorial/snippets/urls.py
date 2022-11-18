"""
Module containing all the urls.
"""

from django.urls import path

from . import views


urlpatterns = [
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail)
]
