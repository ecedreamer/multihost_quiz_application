from django.http import StreamingHttpResponse
import datetime
import time
from quizapp.models import Question
import json

def event_stream():
    old_count = Question.objects.count()
    while True:
        time.sleep(2)
        new_count = Question.objects.count()
        if old_count != new_count:
            old_count = new_count
            dict_data = {
                "new_count": new_count,
                "datetime_now": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            } 
            # yield f'data: Number of question is {new_count} \n\n'
            yield f'data:{json.dumps(dict_data)} \n\n'


def server_sent_event(request):
    
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')