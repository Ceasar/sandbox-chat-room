from django.template import RequestContext, loader
from django.views.decorators.http import require_POST
from django.shortcuts import render_to_response

import pusher

from chatroom.settings import PUSHER_SECRET


def index(request):
    context = RequestContext(request, {})
    return render_to_response('chatroom/index.html', context)


@require_POST
def message(request):
    p = pusher.Pusher(
        app_id='89800',
        key='ceb9e10775a1d1de32b6',
        secret=PUSHER_SECRET,
    )
    p['test_channel'].trigger('test_event', {'message': 'hello world'})
