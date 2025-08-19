from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View """

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch,put, delete)',
            'is similar to a traditional django view',
            'gives you the most control over your app logic',
            'is mapped manually to urls',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    
