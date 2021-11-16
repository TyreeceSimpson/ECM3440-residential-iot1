from mockito import when, mock, verify
import app

class MockClient:
    on_method_request_received = {}
    def send_method_response(method_response):
        return mock({'code': 200, 'text': 'OK'})
    def connect():
        return True
    def send_message(message):
        return True

def test_connect():
    when(app.CounterFitConnection).init('127.0.0.1', 5000).thenReturn(mock(True))
    when(app.IoTHubDeviceClient).create_from_connection_string('HostName=iothub-devices.azure-devices.net;DeviceId=actuator-two;SharedAccessKey=E7PTl7Y99DPl9JSF3rwxvVgsJ++RcReRUs4pCTJ5LuY=').thenReturn(MockClient)
    when(app.device_client).connect().thenReturn(mock(True))
    app.main()
    verify(app.device_client, 1, 1).connect()

def test_handle_request():
    when(app.relay).on().thenReturn(mock(True));
    when(app.relay).off().thenReturn(mock(True));
    app.handle_method_request(mock({'name': 'relay_on'}))
    verify(app.relay, 1, 1).on()
    app.handle_method_request(mock({'name': 'relay_off'}))
    verify(app.relay, 1, 1).off()
