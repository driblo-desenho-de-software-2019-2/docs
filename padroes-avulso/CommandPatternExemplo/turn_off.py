from electronic import ElectronicDevice
from command import Command

class TurnOff(Command):

    def execute(self):
        self.device.turn_off()

    def undo(self):
        self.device.turn_on()

        