from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="latest_article"),
    url(r'^user$', views.user, name="user")
]
