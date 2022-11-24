from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer, FlavourSerializer
from .models import Category, Flavour

# Create your views here.

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FlavourListView(ListAPIView):
    queryset = Flavour.objects.all()
    serializer_class = FlavourSerializer