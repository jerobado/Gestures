# Re-implementing QTableView

from PyQt5.QtWidgets import QTableView
from src.gui.models.tablemodel import GesturesTableModel


class GesturesTableView(QTableView):

    current_data = None
    previous_data = None

    def currentChanged(self, current, previous):
        """ Reimplemented slot that will get the current_data and previous_data. """

        self.current_data = current.data()
        self.previous_data = previous.data()
        self.scrollTo(self.currentIndex())
        print(f'currentChanged -> {self.current_data} x {self.previous_data}')


class NewGesturesTableView(QTableView):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.gesturesTableModel = GesturesTableModel(self)
        self.setModel(self.gesturesTableModel)
        self.horizontalHeader().setStretchLastSection(True)

    def addRecord(self, gesture):

        self.gesturesTableModel.records.append(gesture)
        record_count = len(self.gesturesTableModel.records)
        self.gesturesTableModel.insertRows(record_count, 1)
        self.setModel(self.gesturesTableModel)
