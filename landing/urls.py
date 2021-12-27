from django.urls import path
from .views import home,get_flight_result,get_booking_data
urlpatterns = [
	path('get_booking_data/<str:trace>/',get_booking_data,name='get_booking_data_url'),
	path('get_flight/',get_flight_result,name='flight_result_url'),
	path('',home,name='home_url')
]