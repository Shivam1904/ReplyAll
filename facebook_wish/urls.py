from django.conf.urls import include, url
from django.contrib import admin
from facebook_wish import views
import facebook_wish

urlpatterns = [
    url(r'^$', 'facebook_wish.views.homepage'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^members/', 'facebook_wish.views.get_msg' ),
    url(r'^logout/$', 'facebook_wish.views.logout', name='logout'),
    url(r'^get_msg/$', 'facebook_wish.views.get_msg'),
]
