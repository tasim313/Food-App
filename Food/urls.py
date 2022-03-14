from django.urls import path
from .views import *

app_name = 'Food'

urlpatterns = [
    # path('', item_list, name='item-list'),
    path('', IndexView.as_view(), name='item-list'),
    # path('details/<int:item_id>', item_details, name='item-details'),
    path('details/<pk>', ItemDetails.as_view(), name='item-details'),
    # path('add_item/', create_item, name='add_item'),
    path('add_item/', CreateItem.as_view(), name='add_item'),
    path('update/<id>', update_item, name='update_item'),
    path('delete/<id>/', delete_item, name='delete-item'),
]