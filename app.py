import sys
from PyQt6.QtWidgets import QApplication
from mainwindow import MainWindow
from database import connect_to_database, execute_query

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    sys.exit(app.exec())