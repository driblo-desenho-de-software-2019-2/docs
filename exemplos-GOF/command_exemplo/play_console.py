from class_setters.console_controller import ConsoleController
from invoker import DeviceButton
from command_electronic.turn_off import TurnOff
from command_electronic.turn_on import TurnOn
from command_console.turn_console_standby import TurnConsoleStandby
from command_console.connect_console import ConnectConsole
from command_console.disconnect_console import DisconnectConsole
from command_console.display_console_info import DisplayConsoleInfo

def play_console():
    new_console = ConsoleController().get_device("OFF", "Disconnected")

    on_button = DeviceButton(TurnOn(new_console))
    off_button = DeviceButton(TurnOff(new_console))
    standby_button = DeviceButton(TurnConsoleStandby(new_console))
    connect_button = DeviceButton(ConnectConsole(new_console))
    disconnect_button = DeviceButton(DisconnectConsole(new_console))
    display_button = DeviceButton(DisplayConsoleInfo(new_console))


    display_button.press()
    on_button.press()

    display_button.press()
    connect_button.press()

    display_button.press()
    standby_button.press()

    display_button.press()
    standby_button.pressUndo()

    display_button.press()
    disconnect_button.press()

    display_button.press()
    disconnect_button.pressUndo()

    display_button.press()
    off_button.press()

    display_button.press()

if __name__ == "__main__":
    play_console()