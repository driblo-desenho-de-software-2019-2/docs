from game_console import GameConsole
from command import Command

class DisconnectConsole(Command):

    def execute(self):
        self.device.disconnect_internet()

    def undo(self):
        self.device.connect_internet()