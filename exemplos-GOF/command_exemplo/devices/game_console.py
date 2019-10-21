from devices.electronic import ElectronicDevice

class GameConsole(ElectronicDevice):
    def __init__(self, state, internet_status):
        self.state = state
        self.internet_status = internet_status
    

    def connect_internet(self):
        self.internet_status = "Connected"

    def disconnect_internet(self):
        self.internet_status = "Disconnected"

    def standby(self):
        self.state = "Standby"

    def get_internet(self):
        if self.state == "OFF":
            return "Disconnected"
        else:
            return self.internet_status
