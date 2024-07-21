from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class WeatherTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('get_weather')

    @patch('weather.views.requests.get')
    def test_get_weather_with_mock_data(self, mock_get):
        # 模拟API返回的固定数据
        mock_response = {
            "records": {
                "Station": [
                    {
                        "StationName": "基隆",
                        "WeatherElement": {
                            "AirTemperature": 31.5
                        }
                    },
                    {
                        "StationName": "台北",
                        "WeatherElement": {
                            "AirTemperature": 29.4
                        }
                    }
                ]
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        # 获取响应数据
        response_data = response.json()
        
        # 验证数据格式
        self.assertTrue(isinstance(response_data, list))
        self.assertEqual(len(response_data), 2)

        # 验证温度数据是数值类型
        for station in response_data:
            self.assertIn('stationName', station)
            self.assertIn('temperature', station)
            self.assertIsInstance(station['temperature'], float, f"Temperature is not a float: {station['temperature']}")
