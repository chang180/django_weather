from django.http import HttpResponse

# Create your views here.
import requests
from django.http import JsonResponse
from django.conf import settings

def home(request):
    return HttpResponse("Welcome to the Weather API! Visit /weather/ to get the weather data.")

def get_weather(request):
    api_url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
    params = {
        'Authorization': settings.API_KEY,
    }
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # 如果狀態碼不是200，這將拋出HTTPError
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    data = response.json()
    # 假設我們只需要其中的一些關鍵數據
    weather_data = data.get('records', {}).get('Station', [])
    processed_data = [{
        'stationName': station['StationName'],
        'temperature': station['WeatherElement']['AirTemperature']
    } for station in weather_data]
    
    return JsonResponse(processed_data, safe=False)
