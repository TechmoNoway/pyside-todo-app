from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QPen

class TaskTitleSearchBox(QWidget):
    def __init__(self):
        super().__init__()
        self.search_input = None
        self.search_icon = None
        self.setup_ui()

    def create_search_icon(self):
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        pen = QPen(Qt.gray, 1.5)
        painter.setPen(pen)
        
        painter.drawEllipse(2, 2, 8, 8)
        
        painter.drawLine(9, 9, 13, 13)
        
        painter.end()
        return pixmap

    def setup_ui(self):
        # Main container
        container = QWidget()
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(10, 6, 10, 6)
        container_layout.setSpacing(8)

        # Search icon
        self.search_icon = QLabel()
        search_pixmap = self.create_search_icon()
        self.search_icon.setPixmap(search_pixmap)
        self.search_icon.setFixedSize(16, 16)
        self.search_icon.setStyleSheet("background: transparent; border: none;")

        # Search input
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search")
        self.search_input.setStyleSheet("""
            QLineEdit {
                border: none;
                background: transparent;
                color: white;
                font-size: 14px;
                font-family: 'Segoe UI';
                padding: 2px 0px;
            }
            QLineEdit::placeholder {
                color: #888;
            }
        """)

        container_layout.addWidget(self.search_icon)
        container_layout.addWidget(self.search_input)

        container.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.05);
                border-top: 1px solid #444;
                border-left: 1px solid #444;
                border-right: 1px solid #444;
                border-bottom: 2px solid #555;
                border-radius: 4px;
            }
            QWidget:focus-within {
                border-top: 1px solid #0078d4;
                border-left: 1px solid #0078d4;
                border-right: 1px solid #0078d4;
                border-bottom: 2px solid #0078d4;
                background-color: rgba(0, 120, 212, 0.1);
            }
        """)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(7, 9, 7, 12)
        main_layout.addWidget(container)
        
        self.setLayout(main_layout)

    def get_search_text(self):
        return self.search_input.text().strip()

    def clear_search_text(self):
        self.search_input.clear()