from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QPainter, QPen

class AddTaskInput(QWidget):
    task_added = Signal(str)

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def create_plus_icon(self):
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        pen = QPen(Qt.white, 2)
        painter.setPen(pen)
        
        painter.drawLine(8, 4, 8, 12)
        painter.drawLine(4, 8, 12, 8)  
        
        painter.end()
        return pixmap

    def setup_ui(self):
        container = QWidget()
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)

        # Plus icon
        self.plus_icon = QLabel()
        plus_pixmap = self.create_plus_icon()
        self.plus_icon.setPixmap(plus_pixmap)
        self.plus_icon.setFixedSize(20, 20)

        # Input
        self.input = QLineEdit()
        self.input.setPlaceholderText("Add a task")
        self.input.returnPressed.connect(self.handle_add_task)
        self.input.setStyleSheet("""
            QLineEdit {
                background: transparent;
                border: none;
                color: white;
                font-size: 16px;
                font-family: 'Segoe UI';
                padding: 8px 0px;
            }
            QLineEdit::placeholder {
                color: rgba(255, 255, 255, 0.6);
            }
        """)

        container_layout.addWidget(self.plus_icon)
        container_layout.addWidget(self.input)

        container.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 0.6);
                border-radius: 6px;
                margin: 15px 0px;
                padding: 5px;
            }
            QWidget:hover {
                background-color: rgba(0, 0, 0, 0.7);
            }
        """)

        # main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.addWidget(container)

        self.setLayout(main_layout)

    def handle_add_task(self):
        text = self.input.text().strip()
        if text:
            self.task_added.emit(text)
            self.input.clear()

    def clear_input(self):
        self.input.clear()