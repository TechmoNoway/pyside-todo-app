from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit

class TaskTitleSearchBox(QWidget):
    def __init__(self):
        super().__init__()
        self.search_input = None
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search")
        self.search_input.setStyleSheet("""
            QLineEdit {
                padding: 10px 12px;
                border: 1px solid #555;
                border-radius: 6px;
                background-color: #404040;
                color: white;
                font-size: 14px;
                font-family: 'Segoe UI';
            }
            QLineEdit::placeholder {
                color: #aaa;
            }
            QLineEdit:focus {
                background-color: #333;
                border-color: #0078d4;
            }
        """)

        layout.addWidget(self.search_input)
        self.setLayout(layout)

    def get_search_text(self):
        return self.search_input.text().strip()

    def clear_search_text(self):
        self.search_input.clear()



