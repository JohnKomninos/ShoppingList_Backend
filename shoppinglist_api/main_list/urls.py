from django.urls import path
from . import views

urlpatterns = [
    path('api/items', views.ItemsList.as_view(), name='Items_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/items/<int:pk>', views.ItemsDetail.as_view(), name='items_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
