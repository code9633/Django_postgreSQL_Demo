from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('checkout', views.checkout, name="checkout"),
    path('my_form/', views.my_form_view, name="my_form"), 
    path('success/', views.success_view, name="success"),
    path('report/', views.report_view, name="report")
]
