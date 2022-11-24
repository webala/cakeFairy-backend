from django.urls import path
from .views import CategoryListView, FlavourListView

urlpatterns =[
    path('categories', CategoryListView.as_view(), name='category-list'),
    path('flavours', FlavourListView.as_view(), name='flavour-list'),
]