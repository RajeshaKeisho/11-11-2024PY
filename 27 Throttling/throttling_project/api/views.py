# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import throttle_classes
from .throttling import RegularUserRateThrottle, PremiumUserRateThrottle, ScopeBasedThrottle
from .throttling import GroupBasedThrottle

class HelloWorldView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        return Response({"message": "Hello, World!"})

class RegularUserView(APIView):
    throttle_classes = [RegularUserRateThrottle]

    def get(self, request):
        return Response({"message": "Hello, Regular User!"})

class PremiumUserView(APIView):
    throttle_classes = [PremiumUserRateThrottle]

    def get(self, request):
        return Response({"message": "Hello, Premium User!"})

class ScopedView(APIView):
    throttle_classes = [ScopeBasedThrottle]
    throttle_scope = 'scope1'
    
    def get(self, request):
        return Response({"message": "Scoped Hello, World!"})

class Scope1View(APIView):
    throttle_classes = [ScopeBasedThrottle]
    throttle_scope = 'scope1'

    def get(self, request):
        return Response({"message": "Hello from Scope 1!"})

class Scope2View(APIView):
    throttle_classes = [ScopeBasedThrottle]
    throttle_scope = 'scope2'

    def get(self, request):
        return Response({"message": "Hello from Scope 2!"})

class GroupBasedView(APIView):
    throttle_classes = [GroupBasedThrottle]

    def get(self, request):
        return Response({"message": "Hello, Group-based Throttling!"})
