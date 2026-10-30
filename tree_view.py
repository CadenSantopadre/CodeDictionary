from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt6.QtCore import pyqtSignal

class TreeWidget(QTreeWidget):
    #emit category(str) and name(str)
    selected = pyqtSignal(str, str)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setHeaderLabel("Categories and Snippets") #Make the label at the top the string
        self.itemClicked.connect(self.handle_click) #When clicked, do the handle click method
        self.dic_data = {} #initilaize the data

    def populate(self, data):
        self.clear() #Clear all data first
        self.dic_data = data

        for category, snippets in self.dic_data.items():
            category_item = QTreeWidgetItem(self) #Populate each *item* as a part of the tree itself
            category_item.setText(0, category) #col=0, text is category

            for snippet_name in snippets.keys():
                child_item = QTreeWidgetItem(category_item) #Make it a branch of the category_item
                child_item.setText(0,snippet_name)

        self.expandAll()

    def handle_click(self, item):
        parent=item.parent()#We'll grab the item from the _init_
        if parent:
            category = parent.text(0)
            snippet_name = item.text(0)

            self.selected.emit(category, snippet_name) #Send the signal