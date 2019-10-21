from electronic import ElectronicDevice

class Television(ElectronicDevice):
    def __init__(self, state, volume):
        self.state = state
        self.volume = volume

    def volume_up(self):
        self.volume += 1

    def volume_down(self):
        self.volume -= 1

    def get_volume(self):
        if self.state == "OFF":
            return 0
        else:
            return self.volume