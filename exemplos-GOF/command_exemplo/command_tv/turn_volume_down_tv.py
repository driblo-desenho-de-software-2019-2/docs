from devices.television import Television
from command import Command

class TurnVolumeDownTv(Command):

    def execute(self):
        self.device.volume_down()

    def undo(self):
        self.device.volume_up()