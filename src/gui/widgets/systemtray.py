from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QSystemTrayIcon

from src.gui.widgets.menu import SystemTrayMenu


class GesturesSystemTray(QSystemTrayIcon):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.systemTrayMenu = SystemTrayMenu()

        self.setIcon(QIcon(':/g-key-32.png'))
        self.setContextMenu(self.systemTrayMenu)
