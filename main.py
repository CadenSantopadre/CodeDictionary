import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel

from tree_view import TreeWidget
from display_view import DisplayWidget
from search_view import SearchWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code Dictionary")
        self.resize(800,500)

        self.dic_data = self.load("data.json")

        self.search_bar = SearchWidget()
        self.tree_view = TreeWidget()
        self.display = DisplayWidget()

        self.tree_view.populate(self.dic_data)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Search & View:"))
        left_layout.addWidget(self.search_bar)
        left_layout.addWidget(self.display)

        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Navigation Tree:"))
        right_layout.addWidget(self.tree_view)

        main_layout.addLayout(left_layout, stretch=3)
        main_layout.addLayout(right_layout, stretch=2)
        self.setLayout(main_layout)

        self.tree_view.selected.connect(self.handle_click)
        self.search_bar.searched.connect(self.handle_search)

    def load(self, filename):
        if not os.path.exists(filename):
            return {"Snippets": {"JSON NOT WORKING": "JSON NOT WORKING"}}
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def handle_click(self, category, snippet_name):
        code = self.dic_data.get(category, {}).get(snippet_name, "")
        self.display.show_code(code)

    def handle_search(self, text):
        text = text.lower()
        for category, snippets in self.dic_data.items():
            for snippet_name, code in snippets.items():
                if text in snippet_name.lower():
                    self.display.show_code(code)
                    return

        self.display.show_code(f"No matches found for {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())