from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json

from models import PhotoGallery, VideoGallery, VideoFile
from seafoodservice import settings
from information.views import set_required_data

def gallery(request):
    photos = PhotoGallery.objects.filter(add_this_photo_to_gallery=True)
    videos = []
    for i in VideoGallery.objects.all():
        i_to_dict = i.to_dict()
        x = VideoFile.objects.filter(video=i).values()
        i_to_dict.update({'videos': x})
        videos += [i_to_dict]

    context = {
        "photos": zip(range(1, len(photos)+1), photos),
        "videos": videos
    }
    print context
    context.update(set_required_data(request))
    return render_to_response('gallery.html',
                          context,
                          context_instance=RequestContext(request))


def get_slide_images(request):
    context = {
        "slides": [settings.MEDIA_URL+i.photo.name for i in PhotoGallery.objects.filter(add_this_photo_to_slide=True)],
    }
    return render_to_response('slider_view.html',
                          context,
                          context_instance=RequestContext(request))
