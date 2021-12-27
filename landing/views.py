import os
import pandas as pd
import requests
from django.shortcuts import render
from django.conf import settings

df = pd.read_excel(os.path.join(settings.BASE_DIR,'nexus_airports.xlsx'))

def get_token():
	ip = requests.get('https://api.ipify.org').content.decode('utf8')
	ip_address = format(ip)
	url = "http://api.tektravels.com/SharedServices/SharedData.svc/rest/Authenticate"
	data = {
	"ClientId": "ApiIntegrationNew",
	"UserName": "NEXUSPERFECT",
	"Password": "Nexus@123",
	"EndUserIp": ip_address
	}
	response = requests.post(url,json=data)
	resp = response.json()
	return resp['TokenId'], ip_address

token,ip_address = get_token()


def get_flight(from_,to_,depart,return_,adult,child,class_):
	data = {
	"EndUserIp": ip_address,
	"TokenId": token,
	"AdultCount": str(adult),
	"ChildCount": str(child),
	"InfantCount": "0",
	"DirectFlight": "false",
	"OneStopFlight": "false",
	"JourneyType": "1",
	"Segments": [
		{
		"Origin": from_,
		"Destination": to_,
		"FlightCabinClass": str(class_),
		"PreferredDepartureTime": ""+depart+"T00: 00: 00",
		"PreferredArrivalTime": ""+return_+"T00: 00: 00"
		}
	],
	}
	url = "http://api.tektravels.com/BookingEngineService_Air/AirService.svc/rest/Search"
	response = requests.post(url,json=data)
	resp = response.json()
	return resp

# Create your views here.
def home(request):
	# data = get_flight()
	# dta = data['Response']
	# dt = dta['Results']
	# listl = dt[0]
	# context = {
	# 	'result':listl
	# }
	return render(request,'landing/home.html',{})

def get_flight_result(request):
	if request.method=='POST':
		from_1 = request.POST['from']
		to_1 = request.POST['to']
		result = df[df['city_name']==from_1.title()]
		x = result.airport_code
		y = x.to_list()
		from_ = y[0]
		result = df[df['city_name']==to_1.title()]
		x_1 = result.airport_code
		y_1 = x_1.to_list()
		to_ = y_1[0]
		depart = request.POST['depart']
		return_ = request.POST['return']
		adult = request.POST['adult']
		child = request.POST['child']
		class_ = request.POST['class']

		# print(from_, to_, depart, return_,adult,child,class_)
		data = get_flight(from_,to_,depart,return_,adult,child,class_)
		dta = data['Response']
		dt = dta['Results']
		listl = dt[0]
		trace_id = dta['TraceId']
		context = {
			'result':listl,
			'Trace': trace_id,
			'token':token
		}

		return render(request,'landing/flight_result.html',context)



def get_booking_data(request,trace=None,result_index=None):
	return render(request,'landing/booking_data.html',{})
