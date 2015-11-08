#-*- coding:utf-8 -*-
import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_INCOMING_WEBHOOK_URL = os.environ.get('SLACK_INCOMING_WEBHOOK_URL')