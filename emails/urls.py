from django.urls import path
from . import views

urlpatterns = [
    path('verifey/<uuid:token>/',views.verifey_email_token_view,name='verifey'),
    path('hx/login/',views.email_validation_view,name='login'),
    path('hx/logout/',views.logout_view,name='logout')
]