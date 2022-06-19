import network
from machine import Pin

class Connection:
    def __init__(self, network_name, network_pass):
        self.network_name = network_name
        self.network_pass = network_pass
        self.sta_if = network.WLAN(network.STA_IF)
        self.connect_pin = Pin(2, Pin.OUT)

    def do_connect(self):
        if not self.sta_if.isconnected():
            print('connecting to network...')
            self.sta_if.active(True)
            self.sta_if.connect(self.network_name, self.network_pass)
            while not self.sta_if.isconnected():
                pass
        print('network config:', self.sta_if.ifconfig())
        self.connect_pin.value(True)
      
      
    def do_disconnect(self):
        if self.sta_if.isconnected():
            self.sta_if.active(False)
            print('DISCONNECTED')
            

