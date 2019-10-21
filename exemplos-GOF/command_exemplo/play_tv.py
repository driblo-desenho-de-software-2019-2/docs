from class_setters.tv_remote import TvRemote
from invoker import DeviceButton
from command_electronic.turn_off import TurnOff
from command_electronic.turn_on import TurnOn
from command_tv.turn_volume_down_tv import TurnVolumeDownTv
from command_tv.turn_volume_up_tv import TurnVolumeUpTv
from command_tv.display_tv_info import DisplayTvInfo

def play_tv():
    new_tv = TvRemote().get_device("OFF", 0)

    on_button = DeviceButton(TurnOn(new_tv))
    off_button = DeviceButton(TurnOff(new_tv))
    vol_up_button = DeviceButton(TurnVolumeUpTv(new_tv))
    vol_down_button = DeviceButton(TurnVolumeDownTv(new_tv))
    display_button = DeviceButton(DisplayTvInfo(new_tv))

    display_button.press()
    on_button.press()

    display_button.press()
    vol_up_button.press()

    display_button.press()
    vol_up_button.press()

    display_button.press()
    off_button.press()

    display_button.press()
    off_button.pressUndo()

    display_button.press()
    vol_down_button.press()

    display_button.press()
    vol_down_button.pressUndo()

    display_button.press()

if __name__ == "__main__":
    play_tv()