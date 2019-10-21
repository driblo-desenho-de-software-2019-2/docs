from devices.television import Television
from command_electronic.display_info import DisplayInfo

class DisplayTvInfo(DisplayInfo):

    def execute(self):
        super().execute()
        print(self.device.get_volume())
        print("-----")
        