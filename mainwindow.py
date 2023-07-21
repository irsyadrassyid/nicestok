from PyQt6.QtWidgets import QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Contoh Aplikasi PyQt6")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Klik Saya", self)
        self.button.setGeometry(150, 150, 100, 30)
        self.button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        print("Tombol diklik!")