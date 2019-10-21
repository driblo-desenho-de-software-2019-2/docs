from game_console import GameConsole
from command import Command

class TurnConsoleStandby(Command):

    def execute(self):
        self.device.standby()

    def undo(self):
        self.device.turn_on()