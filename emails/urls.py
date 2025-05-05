from django.urls import path
from . import views

urlpatterns = [
    path('verifey/<uuid:token>/',views.verifey_email_token_view,name='verifey'),
]