from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class TaskList(Base):
    __tablename__ = "task_lists"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="list")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    list_id = Column(Integer, ForeignKey("task_lists.id"))
    list = relationship("TaskList", back_populates="tasks")

