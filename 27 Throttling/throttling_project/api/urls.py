# api/urls.py
from django.urls import path
from .views import HelloWorldView, RegularUserView, PremiumUserView, ScopedView, Scope1View, Scope2View, GroupBasedView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('regular-user/', RegularUserView.as_view(), name='regular_user'),
    path('premium-user/', PremiumUserView.as_view(), name='premium_user'),
    path('scoped/', ScopedView.as_view(), name='scoped_hello_world'),
    path('scope1/', Scope1View.as_view(), name='scope1'),
    path('scope2/', Scope2View.as_view(), name='scope2'),
    path('group-based/', GroupBasedView.as_view(), name='group_based'),
]
