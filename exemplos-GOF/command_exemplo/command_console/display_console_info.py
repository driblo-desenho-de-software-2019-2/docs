from devices.game_console import GameConsole
from command_electronic.display_info import DisplayInfo

class DisplayConsoleInfo(DisplayInfo):

    def execute(self):
        super().execute()
        print(self.device.get_internet())
        print("-----")
