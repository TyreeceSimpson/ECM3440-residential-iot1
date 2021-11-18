from mockito import when, mock, verify
from ..devices import actuator_one_app

class MockClient:
    on_method_request_received = {}
    def send_method_response(method_response):
        return mock({'code': 200, 'text': 'OK'})
    def connect():
        return True
    def send_message(message):
        return True
    
def test_connect():
    when(actuator_one_app.CounterFitConnection).init('127.0.0.1', 5000).thenReturn(mock(True))
    when(actuator_one_app.IoTHubDeviceClient).create_from_connection_string('HostName=iothub-devices.azure-devices.net;DeviceId=actuator-one;SharedAccessKey=Z1ehmmzMSNeQa0qiDyC13msI3Yg/2YnVaIFLY1oN9cU=').thenReturn(MockClient)
    when(actuator_one_app.device_client).connect().thenReturn(mock(True))
    actuator_one_app.main()
    verify(actuator_one_app.device_client).connect()

def test_handle_request():
    when(actuator_one_app.relay).on().thenReturn(mock(True));
    when(actuator_one_app.relay).off().thenReturn(mock(True));
    actuator_one_app.handle_method_request(mock({'name': 'relay_on'}))
    verify(actuator_one_app.relay).on()
    actuator_one_app.handle_method_request(mock({'name': 'relay_off'}))
    verify(actuator_one_app.relay).off()
