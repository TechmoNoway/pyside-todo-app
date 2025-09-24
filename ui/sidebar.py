from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton



class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.my_day_btn = QPushButton("My Day")
        self.important_btn = QPushButton("Important")
        self.planned_btn = QPushButton("Planned")
        self.tasks_btn = QPushButton("Tasks")

        layout.addWidget(self.my_day_btn)
        layout.addWidget(self.important_btn)
        layout.addWidget(self.planned_btn)
        layout.addWidget(self.tasks_btn)
        layout.addStretch()

        self.setLayout(layout)










