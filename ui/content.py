from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QListWidgetItem

from ui.task_item import TaskItemWidget


class Content(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # input add task
        self.input = QLineEdit()
        self.add_btn = QPushButton("Add Task")

        # task list
        self.task_list = QListWidget()

        layout.addWidget(self.input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.task_list)

        self.setLayout(layout)

        # connect signal
        self.add_btn.clicked.connect(self.add_task)

    def add_task(self):
        text = self.input.text().strip()

        if text:
            item = QListWidgetItem(self.task_list)
            widget = TaskItemWidget(text)
            item.setSizeHint(widget.sizeHint())
            self.task_list.setItemWidget(item, widget)
            self.input.clear()















