from django.shortcuts import render_to_response
from django.template import RequestContext


def partners(request):
    context = {}
    return render_to_response(
        'partners.html',
        context,
        context_instance=RequestContext(request))