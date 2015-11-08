#coding: utf-8

import logging

from flask import request, render_template
from todoapps.libs.slack import Message, Response
from todoapps.models import User, Todo
from todoapps import app, db


@app.route('/', methods=['GET'])
def index():
    """ dummy page for checking that Flask is running"""
    return 'healthy'


@app.route('/create_todo', methods=['POST'])
def todo():
    msg = Message.parse(request)
    usr = User(msg.user_name)
    db.session.add(usr)
    todo = Todo('', '', msg.todo_title, 'wip')
    db.session.add(todo)
    db.session.commit()
    bot = Response(msg)
    return bot.response()

@app.route('/show_todo', methods=['GET'])
def show_todo():
    todo = Todo.query.order_by(Todo.id.asc())
    #contents=todoはtemplateに渡す変数
    return render_template('todo/index.html', contents=todo)

if __name__ == "__main__":
    # debugモード
    logging.basicConfig(level=logging.DEBUG)
    app.run()
