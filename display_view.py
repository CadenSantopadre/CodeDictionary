from PyQt6.QtWidgets import QTextEdit

class DisplayWidget(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True) #Don't let us edit the dictionary
        #Give a nice font
        self.setStyleSheet("""
            font-family: 'Courier New', monospace; 
            font-size: 13px;
            background-color: #1e1e1e;
            color: #d4d4d4;
        """)

    def show_code(self, text):
        """Public method to update the code shown."""
        self.setPlainText(text)