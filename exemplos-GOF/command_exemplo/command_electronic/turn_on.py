from devices.electronic import ElectronicDevice
from command import Command

class TurnOn(Command):

    def execute(self):
        self.device.turn_on()

    def undo(self):
        self.device.turn_off()
