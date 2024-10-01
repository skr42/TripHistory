from django.shortcuts import render
from typing import List
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView,DeleteView

from .models import Trip,Note
from django.urls import reverse_lazy
# Create your views here.
class homeview(TemplateView):
    template_name = 'TripsPlan/index.html'


def trip_list(request):
    trips=Trip.objects.filter(owner=request.user)
    context={
        'trips':trips
    }
    return render(request,'TripsPlan/tripsList.html',context)


class TripCreateView(CreateView):
    model=Trip
    success_url = reverse_lazy('trips-list')
    fields=["city","country","start_date","end_date"]
    #looked for the template model_form.html =trip_form
#form owner filed is logged in user
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

class TripDetailView(DetailView):
    model=Trip
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        trip=context["object"]
        notes=trip.notes.all()
        context['notes']=notes
        return context

class NoteDetailsView(DetailView):
        model=Note

class NoteListView(ListView):
    model = Note

    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset
class NoteCreateView(CreateView):
    model=Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"
    def get_form(self):
        form=super(NoteCreateView,self).get_form()
        trips=Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset=trips
        return form


class NoteUpdateView(UpdateView):
    model=Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"
    def get_form(self):
        form=super(NoteUpdateView,self).get_form()
        trips=Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset=trips
        return form

class NoteDeleteView(DeleteView):
    model=Note
    success_url = reverse_lazy('note-list')
    #no html document or we can say no template needed for deleteview ,just have to send the Post request to url

class TripUpdateView(UpdateView):
    model=Trip
    success_url = reverse_lazy('trips-list')
    fields=["city","country","start_date","end_date"]

class TripDeleteView(DeleteView):
    model=Trip
    success_url = reverse_lazy('trips-list')
