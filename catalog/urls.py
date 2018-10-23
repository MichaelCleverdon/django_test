from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from catalog import views

urlpatterns = [
    path('library/', views.showpost, name='library'),

    url(r'^favicon\.ico$', RedirectView.as_view(url='static/images/favicon.ico')),
    path('', views.index, name='index'),

]
