from django.http import HttpResponse
from django.template import RequestContext, loader
import pusher


def index(request):
    template = loader.get_template('chatroom/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def message(request):
    p = pusher.Pusher(
          app_id='89800',
          key='ceb9e10775a1d1de32b6',
          secret='9be17a0bb5d5b5079d79'
    )
    p['test_channel'].trigger('test_event', {'message': 'hello world'})
