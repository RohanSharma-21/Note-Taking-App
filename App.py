import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Note-Taking App")
        self.setGeometry(100, 100, 1920, 1080)
        self.setWindowIcon(QIcon('C:\\Users\\sword\\OneDrive\\Desktop\\VSCODE\\PythonGUIpyqt\\Taking-Notes-Line-Icon-Graphics-14268927-1.jpg'))
        self.init_ui()
        
    def init_ui(self):
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(456, 29, 1405, 1025)
        self.tab_widget.setParent(self)
        
        sidebar = QGroupBox(self)
        sidebar.setGeometry(-3, -3, 400, 1100)
        sidebar.setStyleSheet("background-color: #2C2C2C;")

        self.delete_button = QPushButton("Remove Note                       - ", self)
        self.delete_button.setGeometry(10, 600, 375, 70)
        self.delete_button.setStyleSheet(
        "background-color: #585858; "
        "border-radius: 10px; "
        "font-family: Roboto; "
        "font-size: 25px; "
        "color: white;"
        "font-weight: bold;")
       
        self.note_button = QPushButton("Create Note                       + ", self)
        self.note_button.setGeometry(10, 518, 375, 70)
        self.note_button.setStyleSheet(
        "background-color: #585858; "
        "border-radius: 10px; "
        "font-family: Roboto; "
        "font-size: 25px; "
        "color: white;"
        "font-weight: bold;")
        
        self.note_button.clicked.connect(self.add_note)
        self.delete_button.clicked.connect(self.delete_note)

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("  Search Note...")
        self.search_box.setGeometry(10, 20, 375, 70)
        self.search_box.setStyleSheet(
        "border-radius: 10px; "
        "font-family: Roboto; "
        "font-size: 25px; "
        "color: black;"
        "font-weight: bold;")

        self.results_list = QListWidget(self)
        self.results_list.setGeometry(11, 100, 375, 409)
        self.results_list.setStyleSheet(
        "background-color: #585858;"
        "border-radius: 10px; "
        "font-family: Roboto; "
        "font-size: 30px; "
        "color: white;"
        "font-weight: bold;")

        self.search_box.textChanged.connect(self.update_results)

    def delete_note(self):
        current_index = self.tab_widget.currentIndex()
        if current_index != -1:
            self.tab_widget.removeTab(current_index)

    def add_note(self):
        title, ok = QInputDialog.getText(self, "Create Note", "Enter note title:")
        if ok and title:
            text_edit = QTextEdit()
            text_edit.setStyleSheet("font-family: Helvetica; border: 2px solid white;")
            self.tab_widget.addTab(text_edit, title)
            self.tab_widget.setCurrentWidget(text_edit)

    def save_note_content(self, title, text_edit):
        self.notes[title] = text_edit.toPlainText()
    
    def update_results(self):
        search_text = self.search_box.text().lower()
        self.results_list.clear()

        for i in range(self.tab_widget.count()):
            tab_title = self.tab_widget.tabText(i)
            if search_text in tab_title.lower():
                self.results_list.addItem(tab_title)
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
