class ElectronicDevice:

    def __init__(self, state):
        self.state = state

    def turn_on(self):
        self.state = "ON"

    def turn_off(self):
        self.state = "OFF"

    def get_state(self):
        return self.state
