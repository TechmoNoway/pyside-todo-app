from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QBrush, QPixmap, QColor
from ui.add_task_input import AddTaskInput
from ui.task_item import TaskItem

class Content(QWidget):
    def __init__(self):
        super().__init__()
        self.background_pixmap = None
        self.setup_ui()
        self.setup_background()

    def setup_background(self):
        """Setup background image"""
        try:
            self.background_pixmap = QPixmap("resources/images/eiffel-tower-hd-hf-1920x1080.jpg")
            if self.background_pixmap.isNull():
                print("Could not load background image")
        except Exception as e:
            print(f"Error loading background: {e}")

    def paintEvent(self, event):
        painter = QPainter(self)
        
        if self.background_pixmap and not self.background_pixmap.isNull():
            scaled_pixmap = self.background_pixmap.scaled(
                self.size(), 
                Qt.KeepAspectRatioByExpanding, 
                Qt.SmoothTransformation
            )
            
            # Center the image
            x = (self.width() - scaled_pixmap.width()) // 2
            y = (self.height() - scaled_pixmap.height()) // 2
            painter.drawPixmap(x, y, scaled_pixmap)
            
        else:
            painter.setBrush(QBrush(QColor(74, 155, 142)))
            painter.setPen(Qt.NoPen)
            painter.drawRect(self.rect())

        super().paintEvent(event)

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header section
        header = self.create_header()
        main_layout.addWidget(header)

        # Task list area (scrollable)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }      
        """)

        # Task container
        self.task_container = QWidget()
        self.task_layout = QVBoxLayout(self.task_container)
        self.task_layout.setContentsMargins(0, 0, 0, 0)
        self.task_layout.setSpacing(0)
        self.task_container.setStyleSheet("""
            QWidget {
                background: transparent;
                border: none;
            }      
        """)

        # Add sample tasks
        self.add_sample_tasks()

        # Add stretch to push tasks to top
        self.task_layout.addStretch()

        scroll_area.setWidget(self.task_container)
        main_layout.addWidget(scroll_area)

        # Add task input at bottom
        self.add_task_input = AddTaskInput()
        self.add_task_input.task_added.connect(self.add_task)
        main_layout.addWidget(self.add_task_input)

        self.setLayout(main_layout)

    def create_header(self):
        header_widget = QWidget()
        header_layout = QVBoxLayout()
        header_layout.setContentsMargins(40, 30, 40, 20)
        header_layout.setSpacing(5)

        # Title and icons row
        title_row = QHBoxLayout()
        
        # Title
        title_label = QLabel("My Day")
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 28px;
                font-weight: bold;
                font-family: 'Segoe UI';
            }
        """)

        title_row.addWidget(title_label)
        title_row.addStretch()

        # Action buttons (placeholder icons)
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(10)

        suggestion_btn = QPushButton("💡")
        suggestion_btn.setFixedSize(32, 32)
        suggestion_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 6px;
                color: white;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)

        location_btn = QPushButton("📍")
        location_btn.setFixedSize(32, 32)
        location_btn.setStyleSheet(suggestion_btn.styleSheet())

        more_btn = QPushButton("⋯")
        more_btn.setFixedSize(32, 32)
        more_btn.setStyleSheet(suggestion_btn.styleSheet())

        actions_layout.addWidget(suggestion_btn)
        actions_layout.addWidget(location_btn)
        actions_layout.addWidget(more_btn)

        title_row.addLayout(actions_layout)

        # Date
        date_label = QLabel("Thu 24, 29 Tháng Chín")
        date_label.setStyleSheet("""
            QLabel {
                color: rgba(255, 255, 255, 0.8);
                font-size: 14px;
                font-family: 'Segoe UI';
            }
        """)

        header_layout.addLayout(title_row)
        header_layout.addWidget(date_label)

        header_widget.setLayout(header_layout)
        return header_widget

    def add_sample_tasks(self):
        # Add existing task
        task1 = TaskItem("Go Walking", completed=False, show_star=True)
        self.task_layout.addWidget(task1)

    def add_task(self, task_text):
        """Add a new task to the list"""
        if task_text.strip():
            new_task = TaskItem(task_text.strip())
            # Insert before the stretch
            self.task_layout.insertWidget(self.task_layout.count() - 1, new_task)

    def setup_styles(self):
        self.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }
            QScrollArea > QWidget > QWidget {
                background: transparent;
            }
        """)