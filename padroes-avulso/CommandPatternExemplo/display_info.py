from electronic import ElectronicDevice
from command import Command

class DisplayInfo(Command):

    def execute(self):
        print(self.device.get_state())