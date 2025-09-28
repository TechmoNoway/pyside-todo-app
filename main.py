import sys
from PySide6.QtWidgets import QApplication

from core.database import init_db
from ui.main_window import MainWindow 

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = MainWindow()

    window.setFocus()

    window.show()
    sys.exit(app.exec())



