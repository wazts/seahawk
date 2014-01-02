#! /usr/bin/python
#
#	Kyle Wagner
#	kyle@kaikeru.com
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------------------
from stompest.config import StompConfig
from stompest.protocol import StompSpec
from stompest.sync import Stomp

CONFIG = StompConfig('tcp://localhost:61613')
QUEUE = '/queue/test'

# ------------------------------------------------------------------------------
# IMPLIMINTATIONS
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    client = Stomp(CONFIG)
    client.connect()
    client.subscribe(QUEUE, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL})
    while True:
        frame = client.receiveFrame()
        print 'Got %s' % frame.info()
        print "HEADERS: "
        print frame.headers['destination']
        client.ack(frame)
    client.disconnect()