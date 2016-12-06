# -*- mode: python; coding: utf-8; -*-

from tagging.models import Tag
from django.http import HttpResponse
from django.utils import simplejson

def json_tags(request):
    if request.GET.get('tag'):
        tags = Tag.objects.filter(name__icontains=request.GET.get('tag'))
        jtags = simplejson.dumps([{'caption':x.name,'value':x.name} for x in tags])
    return HttpResponse(jtags or [],mimetype='application/json')
