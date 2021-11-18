from mockito import when, mock, verify
from ..devices import sensor_two_app

class MockClient:
    on_method_request_received = {}
    def send_method_response(method_response):
        return mock({'code': 200, 'text': 'OK'})
    def connect():
        return True
    def send_message(message):
        return True

def test_connect():
    when(sensor_two_app.CounterFitConnection).init('127.0.0.1', 5000).thenReturn(mock(True))
    when(sensor_two_app.IoTHubDeviceClient).create_from_connection_string('HostName=iothub-devices.azure-devices.net;DeviceId=sensor-two;SharedAccessKey=BUccsKmIiv6KVZb0bZzktg72wHl39eqxDPc2FwGzqok=').thenReturn(MockClient)
    when(sensor_two_app.device_client).connect().thenReturn(mock(True))
    sensor_two_app.main()
    verify(sensor_two_app.device_client, 1, 1).connect()

def test_handle_request():
    when(sensor_two_app.relay).on().thenReturn(mock(True))
    when(sensor_two_app.relay).off().thenReturn(mock(True))
    sensor_two_app.handle_method_request(mock({'name': 'relay_on'}))
    verify(sensor_two_app.relay, 1, 1).on()
    sensor_two_app.handle_method_request(mock({'name': 'relay_off'}))
    verify(sensor_two_app.relay, 1, 1).off()
