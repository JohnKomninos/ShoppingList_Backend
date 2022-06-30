from django.urls import path
from . import views

urlpatterns = [
    path('api/sublist', views.SublistList.as_view(), name='sublist_list'),
    path('api/sublist/<int:pk>', views.SublistDetail.as_view(), name='sublist_detail'), 
]
