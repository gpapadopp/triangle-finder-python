import os


class WindowsConsole:
    def clear_console(self):
        os.system("cls")

    def system_pause(self):
        os.system("PAUSE")
