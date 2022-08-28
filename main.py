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

        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCut.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)

    def change_font_size(self, size):
        self.plainTextEdit.setFont(QFont("Courier New", size))

    def undo(self):
        self.plainTextEdit.undo()

    def redo(self):
        self.plainTextEdit.redo()

    def copy(self):
        self.plainTextEdit.copy()

    def cut(self):
        self.plainTextEdit.cut()

    def paste(self):
        self.plainTextEdit.paste()
    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);; Word Doc (*.docx);; "
                                                                         "Python Files(*.py);; All Files (*)",
                                                  options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())
                self.filename = filename

    ## Need to implement save (overwrite) function to save a file over itself with updates.
   # def save_file(self):

    def save_file_as(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);; Word Doc (*.docx);; All Files(*)",
                                                  options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())


    def closeEvent(self, event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)  # 0
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)  # 1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)  # 2

        answer = dialog.exec_()
        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2:
            event.ignore()

def main():
    app = QApplication([])
    window=MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
