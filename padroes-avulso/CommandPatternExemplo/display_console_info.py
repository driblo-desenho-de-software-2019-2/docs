from game_console import GameConsole
from display_info import DisplayInfo

class DisplayConsoleInfo(DisplayInfo):

    def execute(self):
        super().execute()
        print(self.device.get_internet())
        print("-----")