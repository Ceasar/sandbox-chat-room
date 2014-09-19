import threading
import Queue
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.http import require_POST
from django.shortcuts import render_to_response

import pusher

from chatroom.settings import PUSHER_SECRET

q = Queue.Queue()


def index(request):
    context = RequestContext(request, {})
    return render_to_response('chatroom/index.html', context)


def worker():
    p = pusher.Pusher(
        app_id='89800',
        key='ceb9e10775a1d1de32b6',
        secret=PUSHER_SECRET,
    )
    while True:
        data = q.get()
        p['test_channel'].trigger('test_event', data)

thread = threading.Thread(target=worker)
thread.start()


@require_POST
def message(request):
    data = {
        'name': request.POST['name'],
        'message': request.POST['message'],
    }
    q.put(data)
    return HttpResponse(status=204)
