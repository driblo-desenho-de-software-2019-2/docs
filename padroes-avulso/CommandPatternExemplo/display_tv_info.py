from television import Television
from display_info import DisplayInfo

class DisplayTvInfo(DisplayInfo):

    def execute(self):
        super().execute()
        print(self.device.get_volume())
        print("-----")
        