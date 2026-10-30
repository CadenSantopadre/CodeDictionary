from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import pyqtSignal

class SearchWidget(QWidget):
    searched = pyqtSignal(str) #Send signal when searched

    def __init__(self,parent = None):
        super().__init__(parent)
        layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")

        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        self.setLayout(layout)

        self.search_button.clicked.connect(self.emit_search)
        self.search_input.returnPressed.connect(self.emit_search)

    def emit_search(self):
        text = self.search_input.text().strip()
        if text:
            self.searched.emit(text)