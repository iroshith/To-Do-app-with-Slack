# coding: utf-8
from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref
from todoapps import db


class User(db.Model):
    """
    userモデル
    """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(Unicode(255), nullable=False, unique=True)

    #初期化
    def __init__(self, user_name):
        self.user_name = user_name


class Todo(db.Model):
    """
    todoモデル
    """
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    start_date = Column(Unicode(255))
    end_date = Column(Unicode(255))
    todo_title = Column(Unicode(255), ForeignKey('user.user_name'))
    status = Column(UnicodeText)

    #Userとのリレーションを作成
    user = relationship("User", backref=backref('todo', order_by=id))

    #初期化
    def __init__(self, start_date, end_date, todo_title, status):
        self.start_date = start_date
        self.end_date = end_date
        self.todo_title = todo_title
        self.status = status