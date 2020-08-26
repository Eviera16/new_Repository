from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<showid>', views.View),
    path('shows/<showid>/edit', views.edit),
    path('shows/<showid>/delete', views.delete),
    path('shows', views.shows),
    path('shows/update/<showid>', views.update)
]