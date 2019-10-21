from electronic import ElectronicDevice

class Command:
    def __init__(self, device : ElectronicDevice):
        self.device = device

    def execute(self):
        pass

    def undo(self):
        pass
