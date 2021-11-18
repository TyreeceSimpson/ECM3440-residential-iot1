from mockito import when, mock, verify
import actuator_two_app

class MockClient:
    on_method_request_received = {}
    def send_method_response(method_response):
        return mock({'code': 200, 'text': 'OK'})
    def connect():
        return True
    def send_message(message):
        return True

def test_connect():
    when(actuator_two_app.CounterFitConnection).init('127.0.0.1', 5000).thenReturn(mock(True))
    when(actuator_two_app.IoTHubDeviceClient).create_from_connection_string('HostName=iothub-devices.azure-devices.net;DeviceId=actuator-two;SharedAccessKey=E7PTl7Y99DPl9JSF3rwxvVgsJ++RcReRUs4pCTJ5LuY=').thenReturn(MockClient)
    when(actuator_two_app.device_client).connect().thenReturn(mock(True))
    actuator_two_app.main()
    verify(actuator_two_app.device_client, 1, 1).connect()

def test_handle_request():
    when(actuator_two_app.relay).on().thenReturn(mock(True));
    when(actuator_two_app.relay).off().thenReturn(mock(True));
    actuator_two_app.handle_method_request(mock({'name': 'relay_on'}))
    verify(actuator_two_app.relay, 1, 1).on()
    actuator_two_app.handle_method_request(mock({'name': 'relay_off'}))
    verify(actuator_two_app.relay, 1, 1).off()
