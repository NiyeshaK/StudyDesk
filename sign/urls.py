from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signin',views.signin,name="signin"),
     path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout")
]