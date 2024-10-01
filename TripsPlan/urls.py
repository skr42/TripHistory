from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',homeview.as_view(),name="home"),
    path('dashboard/',trip_list,name="trips-list"),
path('dashboard/note/',NoteListView.as_view(),name="note-list"),
    path('dashboard/trip/create/',TripCreateView.as_view(),name="trips-create"),
    path('dashboard/trip/<int:pk>/',TripDetailView.as_view(),name="trip-detail"),
path('dashboard/trip/<int:pk>/delete/',TripDeleteView.as_view(),name="trip-delete"),
path('dashboard/trip/<int:pk>/update/',TripUpdateView.as_view(),name="trip-update"),
path('dashboard/note/<int:pk>/',NoteDetailsView.as_view(),name="note-detail"),
path('dashboard/note/create/',NoteCreateView.as_view(),name="note-create"),
path('dashboard/note/<int:pk>/update/',NoteUpdateView.as_view(),name="note-update"),
path('dashboard/note/<int:pk>/delete/',NoteDeleteView.as_view(),name="note-delete"),





]