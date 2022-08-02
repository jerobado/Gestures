# Initiating spin! ~Cooper, Interstellar, 2014

import logging
import os
import platform
import sys

from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.Qt import PYQT_VERSION_STR
from sip import SIP_VERSION_STR
from src.resources.constant import (__version__,
                                    KEYBOARD_VERSION)
from src.gui.dialogs.messageboxes import DDayMessageBox


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(funcName)s() %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def dislay_welcome_message() -> None:

    message = """
    Gestures, an application for people who just love to type.
    
    Created: 25 Jun 2017
    Author: Jero Bado <tokidokitalkyou@gmail.com>
    """
    print(message)


def display_platform_details() -> None:

    logging.info('Displaying platform details...')
    logging.info(f'User: {os.getlogin()}')
    logging.info(f'Machine: {platform.machine()}')
    logging.info(f'Platform: {platform.platform()}')
    logging.info(f'System: {platform.system()}')


def display_dependency_details() -> None:

    logging.info('Displaying dependency details...')
    logging.info(f'Gestures {__version__}')
    logging.info(f'Python {platform.python_version()}')
    logging.info(f'PyQt {PYQT_VERSION_STR}')
    logging.info(f'keyboard {KEYBOARD_VERSION}')
    logging.info(f'Qt {QT_VERSION_STR}')
    logging.info(f'SIP {SIP_VERSION_STR}')


def valid_license() -> bool:
    """ Check if license expired. """

    # [] TODO: What is the best way to limit its usage?
    return False


if valid_license():   # Gestures' end of usage
    dialog = DDayMessageBox
    if dialog.exec():
        sys.exit(0)
else:
    dislay_welcome_message()
    display_platform_details()
    display_dependency_details()
    # then start executing main.py...
