import logging
from bottle import Bottle, request
from rtkit.parser import RTParser


class NullHandler(logging.Handler):
    def emit(self, record):
        pass
logging.root.addHandler(NullHandler())

app = Bottle(__name__)


@app.post('/ticket/new')
def create_tkt():
    queue_2_response = {
        '1': 'RT/3.8.10 200 Ok\n\n# Ticket 1 created.\n\n',
        '2': 'RT/3.8.10 200 Ok\n\n# Could not create ticket.\n# Could not create ticket. Queue not set\n\n',
        '3': "RT/3.8.10 200 Ok\n\n# Could not create ticket.\n# No permission to create tickets in the queue '___Admin'\n\n"
    }
    form = dict(RTParser.parse(request.forms.get('content', ''), RTParser.decode)[0])
    return queue_2_response[form['Queue']]


@app.get('/ticket/<tid>')
def read_tkt(tid):
    tid_2_response = {
        '1': '''RT/3.8.10 200 Ok

id: ticket/1
Queue: General
Owner: Nobody
Creator: pyrtkit
Subject: pyrt-create4
Status: open
Priority: 5
InitialPriority: 0
FinalPriority: 0
Requestors:
Cc:
AdminCc:
Created: Sun Jul 03 10:48:57 2011
Starts: Not set
Started: Not set
Due: Not set
Resolved: Not set
Told: Wed Jul 06 12:58:00 2011
LastUpdated: Thu Jul 07 14:42:32 2011
TimeEstimated: 0
TimeWorked: 25 minutes
TimeLeft: 0


''',
        '2': 'RT/3.8.10 200 Ok\n\n# Ticket 2 does not exist.\n\n\n',
        '3': 'RT/3.8.10 401 Credentials required\n'
    }
    return tid_2_response[tid]


@app.post('/ticket/<tid>')
def update_tkt(tid):
    form = dict(RTParser.parse(request.forms.get('content', ''), RTParser.decode)[0])
    body = ''
    if form['Queue'] == '3':
        body = 'RT/3.8.10 409 Syntax Error\n\n# queue: You may not create requests in that queue.\n\n'
    return body
