from django.http import StreamingHttpResponse
import datetime
import time


def server_sent_event(request):
    def event_stream():
        while True:
            time.sleep(3)
            yield 'data: The server time is: %s\n\n' % datetime.datetime.now()
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')