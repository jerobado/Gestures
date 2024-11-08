# All of the data that Gestures use will be included in here


import sys
from platform import python_version

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import (PYQT_VERSION_STR,
                          QT_VERSION_STR)
from keyboard import version as KEYBOARD_VERSION

__appname__ = 'Gestures'
__orgname__ = 'Jero Bado'
__orgdomain__ = 'jerobado.com'
__version__ = 'develop-2.1'
__author__ = 'Jero Bado'

APP = QApplication(sys.argv)    # app doesn't run when this is removed
