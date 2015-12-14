from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Certificate
from information.views import set_required_data

def certificates(request):
    list_certificates = Certificate.objects.all()
    context = {"certificates" : zip(range(list_certificates.__len__()), list_certificates)}
    context.update(set_required_data(request))
    return render_to_response('certificates.html', context,
                          context_instance=RequestContext(request))


