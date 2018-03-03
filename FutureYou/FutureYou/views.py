from django.template.loader import get_template
from django.http import HttpResponse


def index(request):
    t = get_template('test.html')
    html = t.render()
    return HttpResponse(html)


def static(request):
    return HttpResponse("hello")