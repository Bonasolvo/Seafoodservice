# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from partners.models import Partner
from gallery.models import PhotoGallery
from information.models import News, MainPage
from information.views import set_required_data


def main(request):
    photos = PhotoGallery.objects.filter(add_this_photo_to_slide=True)
    context = {
        "partners": Partner.objects.all(),
        "slides": photos,
        "main_page": MainPage.objects.all()[0]
    }
    context.update(set_required_data(request))
    return render_to_response(
        'index.html',
        context,
        context_instance=RequestContext(request))
