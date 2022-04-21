from django.shortcuts import render # We will use it later
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Shortener
from .forms import ShortenerForm

def index(request):
    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, 'index.html', context)

    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)
        print(used_form)
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            origin_url= shortened_object.origin_url
             
            context['new_url']  = new_url
            context['long_url'] = origin_url
            return render(request, 'index.html', context)

        context['errors'] = used_form.errors
        return render(request, 'index.html', context)

def redirect_url_view(request, shortened_part):
  
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.save()
        
        return HttpResponseRedirect(shortener.origin_url)
        
    except:
        raise Http404('Sorry this link is broken :(')