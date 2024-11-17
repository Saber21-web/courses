from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('', courses_list, name='courses_list'),
    path('course_detail/<int:pk>/', course_detail, name='course_detail'),
    path('course/buy/<int:course_id>/', course_buy, name='course_buy'),
    path('payment/<int:course_id>/', payment_page, name='payment_page'),
    path('payment/success/<int:course_id>/', payment_success, name='paypal_success'),
    path('payment/cancel/<int:course_id>/', payment_cancel, name='paypal_cancel'),
]
