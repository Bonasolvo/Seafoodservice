from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def contacts(request):
    context = {"contacts":  [
        {
            "contact": employee,
            "skypes": SkypeName.objects.filter(employee=employee),
            "numbers": TelephoneNumber.objects.filter(employee=employee),
            "emails": Email.objects.filter(employee=employee),
        } for employee in Employee.objects.all()
    ]}
    return render_to_response('contacts.html',
                          context,
                          context_instance=RequestContext(request))