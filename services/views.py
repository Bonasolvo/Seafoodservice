from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from transportation.models import TransportationsGeography
from seafoodservice import settings
from  information.views import set_required_data

def services(request):
    points = list(TransportationsGeography.objects.all())
    context = {
        "main_services": Service.objects.filter(is_fundamental_service=True),
        "extra_services": Service.objects.filter(is_fundamental_service=False),
        "transporation_points": zip(range(points.__len__()), points),
        "center_points": settings.GOOGLE_MAPS_SETTINGS,
    }
    context.update(settings.GOOGLE_MAPS_SETTINGS)
    context.update(set_required_data(request))
    return render_to_response('services.html',
                          context,
                          context_instance=RequestContext(request))

