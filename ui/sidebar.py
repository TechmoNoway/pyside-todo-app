from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
from ui.task_title_search_box import TaskTitleSearchBox


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.search_box = None
        self.my_day_btn = None
        self.important_btn = None
        self.planned_btn = None
        self.assigned_btn = None
        self.flagged_btn = None
        self.tasks_btn = None
        self.getting_started_btn = None
        self.setup_ui()
        self.setup_styles()

        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # User profile section
        profile_section = self.create_profile_section()
        layout.addWidget(profile_section)

        # Search box
        self.search_box = TaskTitleSearchBox()
        layout.addWidget(self.search_box)

        # Menu task list
        self.my_day_btn = self.create_menu_button("☀️", "My Day", "1")
        self.important_btn = self.create_menu_button("⭐", "Important")
        self.planned_btn = self.create_menu_button("📅", "Planned")
        self.assigned_btn = self.create_menu_button("👤", "Assigned to me")
        self.flagged_btn = self.create_menu_button("🏳️", "Flagged email")
        self.tasks_btn = self.create_menu_button("📋", "Tasks", "2")

        layout.addWidget(self.my_day_btn)
        layout.addWidget(self.important_btn)
        layout.addWidget(self.planned_btn)
        layout.addWidget(self.assigned_btn)
        layout.addWidget(self.flagged_btn)
        layout.addWidget(self.tasks_btn)
        
        # Custom task list
        custom_section = QVBoxLayout()
        self.getting_started_btn = self.create_menu_button("💡", "Getting started", "7")

        layout.addWidget(self.getting_started_btn)

        layout.addStretch()

        # New list button at bottom
        new_list_btn = self.create_new_list_button()
        layout.addWidget(new_list_btn)

        self.setLayout(layout)
    
    def create_profile_section(self):
        profile_widget = QWidget()
        profile_layout = QHBoxLayout()
        profile_layout.setContentsMargins(12, 12, 12, 12)

        # Avatar (placeholder)
        avatar = QLabel("👤")
        avatar.setFixedSize(32, 32)
        avatar.setStyleSheet("""
            QLabel {
                border-radius: 16px;
                color: white;
                font-size: 16px;
            }
        """)
        avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # User info
        user_info = QVBoxLayout()
        user_info.setSpacing(0)
        
        name_label = QLabel("Kenny Will")
        name_label.setStyleSheet("color: white; font-weight: bold; font-size: 14px;")

        email_label = QLabel("kenny@outlook.com")
        email_label.setStyleSheet("color: #aaa; font-size: 12px;")

        user_info.addWidget(name_label)
        user_info.addWidget(email_label)

        profile_layout.addWidget(avatar)
        profile_layout.addLayout(user_info)
        profile_layout.addStretch()

        profile_widget.setLayout(profile_layout)
        return profile_widget


    def create_menu_button(self, icon, text, count=None):
        btn = QPushButton()
        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(12, 10, 12, 10)

        # Icon
        icon_label = QLabel(icon)
        icon_label.setFixedWidth(20)
        icon_label.setStyleSheet("background-color: transparent")

        # Text
        text_label = QLabel(text)
        text_label.setStyleSheet("color: white; font-size: 14px; background-color: transparent")

        btn_layout.addWidget(icon_label)
        btn_layout.addWidget(text_label)
        btn_layout.addStretch()

        if count:
            count_label = QLabel(count)
            count_label.setStyleSheet("""
                QLabel {
                    background-color: #3d3d3d;
                    color: white;
                    border-radius: 9px;
                    padding: 4px 6px;
                    font-size: 11px;
                }
            """)
            btn_layout.addWidget(count_label)

        btn.setLayout(btn_layout)
        btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                text-align: left;
                padding: 11px 15px;
                margin-top: 3px;
                margin-bottom: 3px;
                margin-left: 5px;
                margin-right: 5px; 
            }
            QPushButton:hover {
                background-color: #262626;
                border-radius: 5px;
            }
            QPushButton:pressed {
                background-color: #555;
            }
        """)

        return btn

    def create_new_list_button(self):
        btn = QPushButton()
        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(12, 10, 12, 10)

        plus_icon = QLabel("+")
        plus_icon.setStyleSheet("color: white; font-size: 16px; font-weight: bold; background-color: transparent;")
        plus_icon.setFixedWidth(20)

        text_label = QLabel("New list")
        text_label.setStyleSheet("color: white; font-size: 16px; background-color: transparent;")

        btn_layout.addWidget(plus_icon)
        btn_layout.addWidget(text_label)
        btn_layout.addStretch()

        btn.setLayout(btn_layout)
        btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                text-align: left;
                padding: 12px 15px;
                margin: 1px;
            }
            QPushButton:hover {
                background-color: #262626;
                border-radius: 5px;
            }
        """)

        return btn

    def setup_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: transparent;
                color: white;
                font-family: 'Segoe UI';
            }
        """)
        self.setFixedWidth(250)
























