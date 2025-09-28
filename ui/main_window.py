from PySide6.QtWidgets import QWidget, QHBoxLayout, QMainWindow

from ui.content import Content
from ui.sidebar import Sidebar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyside")
        self.resize(1280, 720)

        container = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = Sidebar()
        self.content = Content()

        layout.addWidget(self.sidebar, 1)
        layout.addWidget(self.content, 3)

        container.setLayout(layout)
        self.setCentralWidget(container)
