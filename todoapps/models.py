# coding: utf-8
from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime, Boolean
from todoapps import db


class Todo(db.Model):
    """
    todoモデル
    """
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    user_name = Column(Unicode(255), nullable=False)
    todo_title = Column(UnicodeText)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(Boolean)

    #初期化
    def __init__(self, user_name, todo_title, start_date, end_date, status):
        self.user_name = user_name
        self.todo_title = todo_title
        self.start_date = start_date
        self.end_date = end_date
        self.status = status