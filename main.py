from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5 import uic
from PyQt5.QtWidgets import QStyleFactory

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('text_editor.ui', self)
        self.show()

        self.filename = ""
        self.file_name_set = False

        self.plainTextEdit.setFont(QFont("Courier New", 16))
        self.set_light_theme()

        self.setWindowTitle("3writes")
        self.action12pt.triggered.connect(lambda: self.change_font_size(12))
        self.action16pt.triggered.connect(lambda: self.change_font_size(16))
        self.action24pt.triggered.connect(lambda: self.change_font_size(24))
        self.action32pt.triggered.connect(lambda: self.change_font_size(32))

        self.actionNew.triggered.connect(self.new_file)
        self.actionNew.setShortcut(QKeySequence("Ctrl+N"))
        self.actionOpen.triggered.connect(self.open_file)
        self.actionOpen.setShortcut(QKeySequence("Ctrl+O"))
        self.actionSave_As.triggered.connect(self.save_file_as)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave.setShortcut(QKeySequence("Ctrl+S"))
        self.actionClose.triggered.connect(self.close)

        self.actionSelectAll.triggered.connect(self.select_all)
        self.actionSelectAll.setShortcut(QKeySequence("Ctrl+A"))
        self.actionUndo.triggered.connect(self.undo)
        self.actionUndo.setShortcut(QKeySequence("Ctrl+U"))
        self.actionRedo.triggered.connect(self.redo)
        self.actionRedo.setShortcut(QKeySequence("Ctrl+R"))
        self.actionCopy.triggered.connect(self.copy)
        self.actionCopy.setShortcut(QKeySequence("Ctrl+C"))
        self.actionCut.triggered.connect(self.cut)
        self.actionCut.setShortcut(QKeySequence("Ctrl+X"))
        self.actionPaste.triggered.connect(self.paste)
        self.actionPaste.setShortcut(QKeySequence("Ctrl+V"))

        self.actionLight.triggered.connect(self.set_light_theme)
        self.actionDark.triggered.connect(self.set_dark_theme)
        self.actionMatrix.triggered.connect(self.set_matrix_theme)
        self.actionBlack_Gold.triggered.connect(self.set_black_gold_theme)
        self.actionBeach_Boi.triggered.connect(self.set_beach_boi_theme)
        self.actionChickadee.triggered.connect(self.set_chickadee_theme)
        self.actionPink.triggered.connect(self.set_pink_theme)
        self.actionSlate.triggered.connect(self.set_slate_theme)
        self.actionWheat.triggered.connect(self.set_wheat_theme)
        self.actionSilverfox.triggered.connect(self.set_silverfox_theme)

    def change_font_size(self, size):
        self.plainTextEdit.setFont(QFont("Courier New", size))

    def select_all(self):
        self.plainTextEdit.selectAll()

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
        self.file_name_set = False

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

    def set_light_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: white;")
        self.plainTextEdit.setStyleSheet("color: black;")
        self.setStyleSheet("background-color: white;")

    def set_dark_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: #00000080;")
        self.plainTextEdit.setStyleSheet("color: whitesmoke;")
        self.setStyleSheet("background-color: #00000080;")

    def set_matrix_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: black;")
        self.plainTextEdit.setStyleSheet("color: lawngreen;")
        self.setStyleSheet("background-color: black;")

    def set_black_gold_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: black;")
        self.plainTextEdit.setStyleSheet("color: gold;")
        self.setStyleSheet("background-color: black;")

    def set_beach_boi_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: papayawhip;")
        self.plainTextEdit.setStyleSheet("color: lightseagreen;")
        self.setStyleSheet("background-color: papayawhip;")

    def set_chickadee_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: lavenderblush;")
        self.plainTextEdit.setStyleSheet("color: mediumslateblue;")
        self.setStyleSheet("background-color: lavenderblush;")

    def set_pink_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: pink;")
        self.plainTextEdit.setStyleSheet("color: palevioletred;")
        self.setStyleSheet("background-color: pink;")

    def set_slate_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: slategray;")
        self.plainTextEdit.setStyleSheet("color: paleturquoise;")
        self.setStyleSheet("background-color: slategray;")

    def set_wheat_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: wheat;")
        self.plainTextEdit.setStyleSheet("color: darkgoldenrod;")
        self.setStyleSheet("background-color: wheat;")

    def set_silverfox_theme(self):
        self.plainTextEdit.setStyleSheet("background-color: silver;")
        self.plainTextEdit.setStyleSheet("color: whitesmoke;")
        self.setStyleSheet("background-color: silver;")

def main():
    app = QApplication([])
    window=MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()

