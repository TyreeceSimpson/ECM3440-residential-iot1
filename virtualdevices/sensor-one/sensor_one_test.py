from mockito import when, mock, verify
import sensor_one_app

class MockClient:
    on_method_request_received = {}
    def send_method_response(method_response):
        return mock({'code': 200, 'text': 'OK'})
    def connect():
        return True
    def send_message(message):
        return True

def test_connect():
    when(sensor_one_app.CounterFitConnection).init('127.0.0.1', 5000).thenReturn(mock(True))
    when(sensor_one_app.IoTHubDeviceClient).create_from_connection_string('HostName=iothub-devices.azure-devices.net;DeviceId=sensor-one;SharedAccessKey=XH9gycnywIAJM/tQA4wCwh12OgKuRVw4irHS+jPNWuk=').thenReturn(MockClient)
    when(sensor_one_app.device_client).connect().thenReturn(mock(True))
    sensor_one_app.main()
    verify(sensor_one_app.device_client, 1, 1).connect()

def test_handle_request():
    when(sensor_one_app.relay).on().thenReturn(mock(True));
    when(sensor_one_app.relay).off().thenReturn(mock(True));
    sensor_one_app.handle_method_request(mock({'name': 'relay_on'}))
    verify(sensor_one_app.relay, 1, 1).on()
    sensor_one_app.handle_method_request(mock({'name': 'relay_off'}))
    verify(sensor_one_app.relay, 1, 1).off()
