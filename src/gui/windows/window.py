from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from src.gui.dialogs.messageboxes import RemoveMessageBox
from src.gui.widgets.menubar import GesturesMenuBar
from src.gui.widgets.tableview import NewGesturesTableView


class GesturesMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.values = list
        self._set_widgets()
        self._set_properties()
        self._set_connections()

    def _set_widgets(self):

        self.gesturesMenuBar = GesturesMenuBar(self)
        self.gesturesTableView = NewGesturesTableView(self)

        self.setMenuBar(self.gesturesMenuBar)
        self.setCentralWidget(self.gesturesTableView)

    def _set_properties(self):

        self.setWindowTitle('Gestures')
        self.resize(700, 400)

    def _set_connections(self):

        self.gesturesMenuBar.fileMenu.newAction.triggered.connect(self.on_newAction_triggered)
        self.gesturesMenuBar.editMenu.updateAction.triggered.connect(self.on_updateAction_triggered)
        self.gesturesMenuBar.editMenu.deleteAction.triggered.connect(self.on_deleteAction_triggered)

    def on_newAction_triggered(self):

        new_gesture = self.gesturesMenuBar.fileMenu.newAction.keyboardGesture
        if not new_gesture.empty():
            self.gesturesTableView.addRecord(new_gesture)

    def on_updateAction_triggered(self):

        selected_index = self.gesturesTableView.currentIndex()
        self.gesturesMenuBar.editMenu.updateAction.showUpdateGestureDialog(selected_index)

        update_gesture = self.gesturesMenuBar.editMenu.updateAction.keyboardGesture
        if not update_gesture.empty():
            self.gesturesTableView.updateRecord(selected_index.row(), update_gesture)

    def on_deleteAction_triggered(self):

        selected_index = self.gesturesTableView.currentIndex()
        print('selected_index: ', selected_index.row(), selected_index.column())

        choice = RemoveMessageBox.exec()
        if choice == RemoveMessageBox.Yes:
            self.gesturesTableView.removeRecord(selected_index.row())
