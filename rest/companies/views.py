from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

# Create your views here.
#list's stocks or creates new stock
class StockList(APIView):
    def get(self):
        pass

    def post(self):
        pass