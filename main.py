from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('text_editor.ui', self)
        self.show()

        self.filename = ""
        self.file_name_set = False

        self.plainTextEdit.setFont(QFont("Courier New", 16))

        self.setWindowTitle("3writes")
        self.action12pt.triggered.connect(lambda: self.change_font_size(12))
        self.action16pt.triggered.connect(lambda: self.change_font_size(16))
        self.action24pt.triggered.connect(lambda: self.change_font_size(24))
        self.action32pt.triggered.connect(lambda: self.change_font_size(32))

        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave_As.triggered.connect(self.save_file_as)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(self.close)

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

    def new_file(self, event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)  # 0
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)  # 1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)  # 2

        answer = dialog.exec_()
        if answer == 0: # if yes is clicked
            self.save_file_as() # saves file
        elif answer == 2: # if cancel is clicked
            dialog.close() # close dialog box
            return 0 # return 0, so clear() func below is not triggered

        self.plainTextEdit.clear() # after file is saved, or not, text window is cleared
        self.filename = ""

    def open_file(self):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)  # 0
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)  # 1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)  # 2

        answer = dialog.exec_()
        if answer == 0: # if yes is clicked
            self.save_file_as() # saves file
        elif answer == 2: # if cancel is clicked
            dialog.close() # close dialog box
            return 0 # return 0, so clear() func below is not triggered

        options = QFileDialog.Options()  # default
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);; Word Doc (*.docx);; "
                                                                         "Python Files(*.py);; All Files (*)",
                                                  options=options)
        if self.filename != "":  # basically, if an actual file is selected
            with open(self.filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())  # set contents of text window to file contents
                self.file_name_set = True  # used in save logic

    def save_file_as(self):
        options = QFileDialog.Options()  # default
        self.filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);; Word Doc (*.docx);; All Files(*)",
                                                  options=options)
        if self.filename != "":  # basically, if an actual file is selected
            with open(self.filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())  # set file contents to contents of text window
                self.file_name_set = True  # used in save logic

    def save_file(self):
        if self.file_name_set:  # meaning, if a file has been opened, or "saved as", and is therefore NOT a new file
            with open(self.filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())  # overwrite file contents with contents of the text window
        else:  # meaning a file has not been opened or saved as... NEW files!
            self.save_file_as()  # redirect to save as func

    def closeEvent(self, event):  # used when exiting window
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)  # 0
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)  # 1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)  # 2

        answer = dialog.exec_()
        if answer == 0:  # yes
            self.save_file_as()  # save file as
            event.accept()
        elif answer == 2:  # cancel, return to work.
            event.ignore()

def main():
    app = QApplication([])
    window=MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
