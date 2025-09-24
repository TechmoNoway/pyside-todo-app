from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel, QPushButton



class TaskItemWidget(QWidget):
    def __init__(self, task_text: str):
        super().__init__()
        layout = QHBoxLayout()

        self.checkbox = QCheckBox()
        self.label = QLabel(task_text)
        self.delete_btn = QPushButton("X")

        layout.addWidget(self.checkbox)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.delete_btn)

        self.setLayout(layout)










