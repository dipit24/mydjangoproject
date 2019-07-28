from django.urls import path,include
from ClassBasedViews import views
from django.shortcuts import render

urlpatterns=[
    path('',views.IndexView.as_view(),name="indexCBV"),
    path('blogs/',views.BlogsListView.as_view(),name='blog'),
    path('blogscreate/',views.BlogCreateView.as_view(),name='createblog')
    ]
    