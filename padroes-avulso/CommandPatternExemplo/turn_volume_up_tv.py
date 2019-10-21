from television import Television
from command import Command

class TurnVolumeUpTv(Command):

    def execute(self):
        self.device.volume_up()

    def undo(self):
        self.device.volume_down()