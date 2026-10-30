import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create a Dictionary Entry") #Set title
        self.resize(300, 300)

        self.filename = "data.json" #Set instance varible
        self.dic_data = self.load(self.filename)

        layout = QVBoxLayout() #Give a vertical layout

        #Must have self. so we can "Read" it during submission
        self.category_widget = QLineEdit()
        self.category_widget.setPlaceholderText("Category")
        self.category_widget.setMaximumHeight(50)
        layout.addWidget(self.category_widget)

        self.title_widget = QLineEdit()
        self.title_widget.setPlaceholderText("Title")
        self.title_widget.setMaximumHeight(50)
        layout.addWidget(self.title_widget)

        self.text_widget = QTextEdit()
        self.text_widget.setPlaceholderText("Text")
        self.text_widget.setMinimumSize(300, 200)
        layout.addWidget(self.text_widget)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.handle_submission)
        layout.addWidget(submit_button)
        
        self.setLayout(layout)

    def load(self, filename):
        if not os.path.exists(filename):
            return {"Snippets": {"JSON NOT WORKING": "JSON NOT WORKING"}}
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def handle_submission(self):
        #Extract text
        category = self.category_widget.text().strip()
        title = self.title_widget.text().strip()
        text = self.text_widget.toPlainText().strip()

        if not category or not title or not text: #Check if they are blank
            QMessageBox.warning(self, "Submission Error", "All fields must be filled out.") #Parent is self, title is SE, text is all fields..
            return

        if category not in self.dic_data:
            self.dic_data[category] = {} #Put in root if not a category

        self.dic_data[category][title] = text

        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.dic_data, f, ensure_ascii=False, indent=4)
            
            QMessageBox.information(self, "Success", f"Saved entry '{title}' under category '{category}'!")
            
            self.category_widget.setText("")
            self.title_widget.setText("")
            self.text_widget.setPlainText("")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
