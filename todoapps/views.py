#coding: utf-8

import logging

from flask import request, render_template, flash, redirect, url_for
from todoapps.libs.slack import Message, Response, response_end
from todoapps.models import Todo
from todoapps import app, db
from datetime import datetime, timedelta


@app.route('/', methods=['GET'])
def index():
    """ dummy page for checking that Flask is running"""
    return 'healthy'


@app.route('/create_todo', methods=['POST'])
def create_todo():
    msg = Message.parse(request)
    todo = Todo(msg.user_name, msg.text, msg.timestamp, msg.timestamp, True)
    db.session.add(todo)
    db.session.commit()
    flash('New todo was successfully created')
    # slackにタスクに登録したメッセージを送る
    bot = Response(msg)
    return bot.response_start()


@app.route('/show_todo/<username>', methods=['GET'])
def show_todo(username):
    todo = Todo.query.filter_by(user_name=username).all()
    #contents=todoはtemplateに渡す変数
    return render_template('todo/index.html', contents=todo)


@app.route('/show_todo?username=<username>', methods=['POST'])
def update_todo(username):
    values = request.form.getlist('check')
    #JSTに変換
    now = datetime.now() + timedelta(hours=9)
    for v in values:
        active_todo = Todo.query.filter_by(id=int(v)).first()
        if not active_todo is None:
            active_todo.status = False
            active_todo.end_date = now
            db.session.add(active_todo)
            db.session.commit()
            flash('Todo was successfully updated')
            # slackに終了メッセージを送る
            took_time = now - active_todo.start_date
            title = active_todo.todo_title
            response_end(title, took_time)
    return redirect(url_for('show_todo', username=username))


if __name__ == "__main__":
    # debugモード
    logging.basicConfig(level=logging.DEBUG)
    app.run()
