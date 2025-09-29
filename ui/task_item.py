from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel, QPushButton, QVBoxLayout

class TaskItem(QWidget):
    def __init__(self, text, completed=False, show_star=False):
        super().__init__()
        self.text = text
        self.completed = completed
        self.show_star = show_star
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(40, 8, 40, 8)
        layout.setSpacing(12)

        # Checkbox
        self.checkbox = QCheckBox()
        self.checkbox.setChecked(self.completed)
        self.checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 9px;
                border: 2px solid rgba(255, 255, 255, 0.6);
                background-color: transparent;
            }
            QCheckBox::indicator:checked {
                background-color: #0078d4;
                border-color: #0078d4;
            }
        """)

        # Task text
        self.task_label = QLabel(self.text)
        self.task_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
                font-family: 'Segoe UI';
                background: transparent;
            }
        """)

        # Category label (if any)
        self.category_label = QLabel("Tasks")
        self.category_label.setStyleSheet("""
            QLabel {
                color: rgba(255, 255, 255, 0.6);
                font-size: 12px;
                font-family: 'Segoe UI';
            }
        """)

        layout.addWidget(self.checkbox)
        
        # Text container
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        text_layout.addWidget(self.task_label)
        text_layout.addWidget(self.category_label)
        
        layout.addLayout(text_layout)
        layout.addStretch()

        # Star button (if needed)
        if self.show_star:
            star_btn = QPushButton("⭐")
            star_btn.setFixedSize(24, 24)
            star_btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    border: none;
                    color: rgba(255, 255, 255, 0.6);
                    font-size: 16px;
                }
                QPushButton:hover {
                    color: white;
                }
            """)
            layout.addWidget(star_btn)

        self.setStyleSheet("""
            TaskItem {
                background-color: rgba(0, 0, 0, 0.6);
                border-radius: 8px;
                margin: 5px 0px;
                padding: 5px;
            }
            TaskItem:hover {
                background-color: rgba(0, 0, 0, 0.7);
            }
        """)

        self.setLayout(layout)