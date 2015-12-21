from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#document_root=settings.MEDIA_ROOT
urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':'media'}),
    url(r'^art$', views.art, name='art'),
    url(r'^design$', views.design, name='design'),
    url(r'^backfeed$', views.backfeed, name='backfeed'),
    url(r'^about$', views.about, name='about'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
