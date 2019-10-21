from game_console import GameConsole
from command import Command

class ConnectConsole(Command):

    def execute(self):
        self.device.connect_internet()

    def undo(self):
        self.device.disconnect_internet()