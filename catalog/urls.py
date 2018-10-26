from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from catalog import views

urlpatterns = [
    path('library/', views.show_post, name='library'),
    path('post/<int:pk>/', views.postDetail, name='post_detail'),
    path('post/new/', views.postNew, name='post_new'),
    path('post/edit/', views.postEdit, name="post_edit"),
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/images/favicon.ico')),
    path('', views.index, name='index'),

]
