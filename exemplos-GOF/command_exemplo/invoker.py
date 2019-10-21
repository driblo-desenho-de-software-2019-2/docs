from command import Command

class DeviceButton:
    
    def __init__(self, command: Command):
        self.command = command

    def press(self):
        self.command.execute()

    def pressUndo(self):
        self.command.undo()
