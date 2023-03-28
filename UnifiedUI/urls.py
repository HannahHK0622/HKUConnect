from django.urls import path
from . import views

app_name = 'UnifiedUI'

urlpatterns = [
    path('', views.authenticate, name='index'),
    # path('signup/', views.signup_view, name='sign up'),
]