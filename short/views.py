from django.shortcuts import render
from .models import Shortener
from .forms import ShortForm
from django.http import HttpResponseRedirect

def shortenerView(request, slug=None):
    if slug:

        return HttpResponseRedirect(Shortener.objects.get(slug=slug).link)

    form = ShortForm(request.POST or None)

    if form.is_valid():
        Shortener.objects.create(slug=form.cleaned_data.get('slug'), link=form.cleaned_data.get('link'))

    content = {
        'form':form
    }

    return render(request, 'index.html', content)
