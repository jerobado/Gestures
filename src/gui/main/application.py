import ctypes
import sys
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon
from src.gui.windows.window import GesturesMainWindow
from src.gui.widgets.systemtray import GesturesSystemTray
from src.resources.constant import __appname__, __version__, __orgname__, __orgdomain__


class GesturesMainApplication(QApplication):

    def __init__(self):

        super().__init__(sys.argv)
        self._set_associated_windows_in_taskbar()
        self.setOrganizationName(__orgname__)
        self.setOrganizationDomain(__orgdomain__)
        self.setApplicationName(__appname__)
        self.setApplicationVersion(__version__)
        self.setStyle('windowsvista')

        self.window = GesturesMainWindow()

        # TODO: move back to GesturesMainWindow class
        self.systemTray = GesturesSystemTray(self.window)
        self.systemTray.setToolTip(f'{self.applicationName()} {self.applicationVersion()}')

        self.systemTray.activated.connect(self.on_systemTray_activated)
        self.systemTray.systemTrayMenu.openAction.triggered.connect(self.window.show)
        self.systemTray.systemTrayMenu.newAction.triggered.connect(self.window.on_newAction_triggered)
        self.systemTray.systemTrayMenu.quitAction.triggered.connect(self.closeAllWindows)
        self.systemTray.systemTrayMenu.quitAction.triggered.connect(self.quit)

    def _set_associated_windows_in_taskbar(self):
        """ Group associated processes and windows under a single taskbar button. """

        app_id = f'{__orgdomain__}.{__appname__}.{__version__}'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    def on_systemTray_activated(self, reason: QSystemTrayIcon):

        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.window.show()

    def run(self):

        self.window.hook(key_listener)
        self.window.show()
        self.systemTray.show()
        self.exec()


def key_listener(event):

    if event.event_type == 'down':
        print(f'{event.name=}')
