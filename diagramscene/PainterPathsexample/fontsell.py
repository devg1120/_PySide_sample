from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QFontDialog
from PySide6.QtGui import QFont

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("pyQt6 sample")
        
        self.button1 = QPushButton('Select Font')
        self.button1.clicked.connect(self.showDialog1)

        self.setCentralWidget(self.button1)
    
    def showDialog1(self):

        ok, font = QFontDialog.getFont(QFont(), self, "Select font")

if __name__ == "__main__":
    app = QApplication([])
    ex =Window()
    ex.show()
    app.exec()

