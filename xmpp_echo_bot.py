#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sleekxmpp

# Python versions before 3.0 do not use UTF-8 encoding
# by default.
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input

class EchoBot(sleekxmpp.ClientXMPP):
    def __init__(self, jid, password, message_text):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        self.message_text = message_text
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.send_message)

    def start(self, event):
        self.send_presence()
        self.get_roster()

    def send_message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            msg.reply(self.message_text).send()

if __name__ == '__main__':
    message = """Blub"""
    xmpp = EchoBot(jid, password, message)

    if xmpp.connect():
        # For example, to use Google Talk you would
        # need to use: if xmpp.connect(('talk.google.com', 5222)):
        xmpp.process(block=True)
        print("Done")
    else:
        print("Unable to connect.")
