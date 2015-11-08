#coding: utf-8
from flask import jsonify
from ..config import SLACK_TOKEN

class Message(object):
    """Slackのメッセージクラス"""
    def __init__(self):
        self.token = SLACK_TOKEN

    @classmethod
    def parse(cls, request):
        params = request.form
        msg = cls()
        try:
            msg.team_id = params['team_id']
            msg.channel_id = params['channel_id']
            msg.channel_name = params['channel_name']
            msg.timestamp = params['timestamp']
            msg.user_id = params['user_id']
            msg.user_name = params['user_name']
            msg.trigger_word = params['trigger_word']

            msg.args = params['text'].split()
            if len(msg.args) > 0:
                msg.command = msg.args[0]
                msg.text = ''.join(msg.args[1:])
            else:
                msg.text = params['text']

        except Exception, emg:
            print emg
        return msg

    def __str__(self):
        res = self.__class__.__name__
        res += "@{0.token}[channel={0.channel_name}, user={0.user_name}, text={0.text}]".format(self)
        return res


class Response(object):
    def __init__(self, msg):
        self.msg = msg
        self._ICON = ':information_desk_person:'
        self._NAME = 'arisa'

    def response(self):
        # slackbotによる発言を無視するため
        if self.msg.command == 'slackbot':
            return ''
        else:
            txt = u'{0}をタスクに積んどいたよ。頑張ってね！'.format(self.msg.text)
            return jsonify({
                'text': txt,
                'username': self._NAME,
                'icon_emoji': self._ICON
            })
