from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json
from django.utils.translation import ugettext_lazy as _

from models import *
from information.views import set_required_data
from forms import LeaveMessageForm

def contacts(request):
    context = {}
    if request.POST:
        form = LeaveMessageForm(request.POST)
        print form
        if form.is_valid():
            form.save()
            context['notifications_messages']=[_(u"Thank you, we received your message.")]
            form = LeaveMessageForm()
        else:
            context['notifications_messages']=[_(u"Form is not valid!\nPlease correct your errors bellow.")]
    else:
        form = LeaveMessageForm()
    context['form'] = form
    context.update(dict(contacts=[{
                                 "contact": employee,
                                 "skypes": SkypeName.objects.filter(contact=employee),
                                 "numbers": TelephoneNumber.objects.filter(contact=employee),
                                 "emails": Email.objects.filter(contact=employee)}
                                for employee in Employee.objects.all()],
                   office_contacts=[dict(contact=office, skypes=SkypeName.objects.filter(contact=office),
                                         numbers=TelephoneNumber.objects.filter(contact=office),
                                         emails=Email.objects.filter(contact=office),
                                         faxs=FaxNumber.objects.filter(contact=office))
                                    for office in OfficeContact.objects.all()])
    )
    context.update(set_required_data(request))

    return render_to_response('contacts.html',
                          context,
                          context_instance=RequestContext(request))

