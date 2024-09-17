from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import warrior
# create your views here.

def warprofile (request, wid):
    w = get_object_or_404(warrior, pk=wid)
    template = loader.get_template('game/warprofile.html')

    context = {
        'warrior': w,  # Pass the warrior object to the template
    }
    return HttpResponse(template.render(context,request))


