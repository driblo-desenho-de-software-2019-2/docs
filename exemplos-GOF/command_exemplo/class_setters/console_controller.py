from devices.game_console import GameConsole
class ConsoleController:

    def get_device(self, state, internet_status):
        return GameConsole(state, internet_status)