from django.shortcuts import render
from .models import Film
from django.views.generic import DetailView, CreateView
from .forms import FilmForm
from django.urls import reverse_lazy
from django.utils import timezone



def film_list(request):
    films = Film.objects.all
    return render(request, 'film/film_list.html', {'films': films})

class FilmDetailView(DetailView):
    model = Film
    template_name = 'film/film_detail.html'
    context_object_name = 'film'

class FilmAddView(CreateView):
    template_name ='blog/film_edit.html'
    model = Film
    form_class = FilmForm
    success_url = reverse_lazy('film_list')

    def form_valid(self, form):
        feilds = form.save(commit=False)
        feilds.release_date = timezone.now()
        feilds.save()
        return super().form_valid(form)