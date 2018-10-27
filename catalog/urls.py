from django.conf.urls import url
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from django.contrib import admin

from catalog import views

urlpatterns = [

    path('post/<int:pk>/', views.postDetail, name='post_detail'),
    path('post/new/', views.postNew, name='post_new'),
    path('post/edit/', views.postEdit, name="post_edit"),
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/images/favicon.ico')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),

]
