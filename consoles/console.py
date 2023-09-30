import sys
from consoles.linux_console import LinuxConsole
from consoles.mac_os_console import MacOsConsole
from consoles.windows_console import WindowsConsole


class Console:
    def __init__(self):
        self.linux_console = LinuxConsole()
        self.mac_os_console = MacOsConsole()
        self.windows_console = WindowsConsole()

    def clear_console(self):
        if sys.platform == 'linux':
            self.linux_console.clear_console()
        elif sys.platform == 'win32':
            self.windows_console.clear_console()
        elif sys.platform == 'darwin':
            self.mac_os_console.clear_console()

    def pause_system(self):
        if sys.platform == 'linux':
            self.linux_console.system_pause()
        elif sys.platform == 'win32':
            self.windows_console.system_pause()
        elif sys.platform == 'darwin':
            self.mac_os_console.system_pause()
