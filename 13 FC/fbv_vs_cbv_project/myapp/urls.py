from django.urls import path
from .views import ItemListView, ItemDetailView,  ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    # FBV URLs
    # path('fbv/items/', item_list, name='fbv_item_list'),
    # path('fbv/items/<int:pk>/', item_detail, name='fbv_item_detail'),
    # path('fcreate/', item_create_view, name='item_create_fbv'),  # FBV
    # path('<int:pk>/edit/', item_update, name='item-update'),
    # path('<int:pk>/delete/', item_delete, name='item-delete'),

    # CBV URLs
    path('cbv/items/', ItemListView.as_view(), name='cbv_item_list'),
    path('cbv/items/<int:pk>/', ItemDetailView.as_view(), name='cbv_item_detail'),    
    path('ccreate/', ItemCreateView.as_view(), name='item_create_cbv'),  # CBV
    path('cbv/<int:pk>/edit/', ItemUpdateView.as_view(), name='item-update'),
    path('cbv/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]
