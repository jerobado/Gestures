""" Gestures: an application for people who just loved to type.

    Interface: GUI (PyQt5)
    Language: Python 3.6.6
    Created: 25 Jun 2017
    Author: mokachokokarbon
 """

from src.gui.main.application import GesturesMainApplication


if __name__ == '__main__':

    app = GesturesMainApplication()
    app.run()


# TODO: convert resources.qrc to PyQt6 version,
#  see https://stackoverflow.com/questions/66099225/how-can-resources-be-provided-in-pyqt6-which-has-no-pyrcc