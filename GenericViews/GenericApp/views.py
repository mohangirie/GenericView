from django.shortcuts import render
from django.views import generic
from .models import Generic
from .forms import GenericForms

# Create your views here.


def makeentry(request):
    if request.method == 'POST':
        form = GenericForms(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            desc = request.POST.get('desc', '')
            person = Generic(name=name, desc=desc)
            person.save()
            form = GenericForms()
            return render(request, 'genericviews/makeentry.html', {'form': form})
    else:
        form = GenericForms()
        return render(request, 'genericviews/makeentry.html', {'form': form})


class IndexView(generic.ListView):
    context_object_name = 'list'
    template_name = 'genericviews/index.html'

    def get_queryset(self):
        return Generic.objects.all()


class DetailsView(generic.DetailView):
    model = Generic
    template_name = 'genericviews/detail.html'
