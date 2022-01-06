from django.shortcuts import render
from .serializers import AccountSerializer
from .models import Account
from django.conf import settings
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response



class AccountViewSet(viewsets.ModelViewSet):
    "API endpoint for listing and creating accounts"
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
  

class AccountDetails(viewsets.ViewSet):
    def retrieve(self, request, id=None):
        queryset = Account.objects.all()
        account = get_object_or_404(queryset, id=id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    def update(self, request, id=None):
    
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account, data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
  
  
    def destroy(self, request, id=None):
        account = Account.objects.get(id=id)
        account.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 
  
  
