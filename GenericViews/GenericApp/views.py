from django.shortcuts import render
from django.views import generic
from .models import Generic
from .forms import GenericForms

# Create your views here.

def makeentry(request):
    if request.method=='POST':
        form = GenericForms(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            desc = request.POST.get('desc', '')
            person = Generic(name=name,desc=desc)
            person.save()
            form = GenericForms()
            return render(request,'genericviews/makeentry.html', {'form': form})
    else:
        form = GenericForms()
        return render(request, 'genericviews/makeentry.html', {'form': form})

