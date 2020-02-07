from django.shortcuts import render
from .forms import URLForm


# Create your views here.

def index(request):
    form = URLForm()
    return render(request, 'linkshortcutter/index.html', context={'form': form})
