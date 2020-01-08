from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, DeleteView
from .models import Artwork

# Create your views here.

def index(request):
    return render(request, 'index.html' )


class ArtListView(ListView):
    model = Artwork
    template_name = 'list.html'

    def get(self, request):
        artworks = self.get_queryset().all()
        return render(request, self.template_name, {'artworks': artworks})


class ArtDetailView(DetailView):
    model = Artwork
    template_name = 'details.html'

    def get(self, request, slug):
        artwork = self.get_queryset().filter(slug__iexact=slug)

        return render(request, self.template_name, {'artwork': artwork})

class ArtListByTagView(ListView):
    model = Artwork
    template_name = 'list.html'

    def get(self, request, tag):
        artworks = self.get_queryset().filter(tag=tag)
        return render(request, self.template_name, {'artworks': artworks})

