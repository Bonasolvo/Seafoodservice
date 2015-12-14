from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _


import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^captcha/', include('captcha.urls')),
)

#pages
urlpatterns += patterns('pages.views',
    url(r'^$', 'main', name='home'),
)

#services
urlpatterns += patterns('services.views',
    url(r'^services/$', 'services', name='services'),
)

#contacts
urlpatterns += patterns('contacts.views',
    url(r'^contacts/$', 'contacts', name='contacts'),
)

#news
urlpatterns += patterns('information.views',
    url(r'^news/$', 'news', name='news'),
    url(r'^news/(?P<news_id>\d+)/$', 'news_item', name='news_item'),
    url(r'^useful-information/$', 'useful_information', name='usefull_information'),
    url(r'^useful-information/(?P<information_id>\d+)/$', 'useful_information_item', name='usefull_information_item'),
)

#gallery
urlpatterns += patterns('gallery.views',
    url(r'^gallery/$', 'gallery', name='gallery'),
    url(r'^get_slide_images/$', 'get_slide_images', name='get_slide_images'),
)

#certificates
urlpatterns += patterns('certificates.views',
    url(r'^certificates/$', 'certificates', name='certificates'),
)
