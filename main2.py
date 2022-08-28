from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('text_editor.ui', self)
        self.show()

        self.setWindowTitle("3writes")
        self.action12pt.triggered.connect(lambda: self.change_font_size(12))
        self.action16pt.triggered.connect(lambda: self.change_font_size(16))
        self.action24pt.triggered.connect(lambda: self.change_font_size(24))
        self.action32pt.triggered.connect(lambda: self.change_font_size(32))

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave_As.triggered.connect(self.save_file_as)

    def change_font_size(self, size):
        self.plainTextEdit.setFont(QFont("Courier New", size))

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);; Python Files(*.py)",
                                                  options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    ## Need to implement save (overwrite) function to save a file over itself with updates.

    def save_file_as(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);; Word Doc (*.docx);; All Files(*)",
                                                  options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

def main():
    app = QApplication([])
    window=MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
