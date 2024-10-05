from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
#from django.template import loader
from .models import warrior,Spell
from django.contrib.auth.models import User

# create your views here.

class WarProfile(generic.DetailView):
    model = warrior #why template should be in hiroes, no in the template directory???!!!

#def warprofile (request, wid):
#    w = get_object_or_404(warrior, pk=wid)
#    #template = loader.get_template('game/warprofile.html')
#
#    context = {
#        'warrior': w,
#    }
#    #return HttpResponse(template.render(context,request))
#    return render(request, 'game/warprofile.html', context)

def army(request, userid):
    user = get_object_or_404(User, pk = userid)
    warriors = warrior.objects.filter(user = user)
    image = warrior.objects.filter(user=user)
    #w = warrior.objects.all()[0]
    #w2 = warrior.objects.all()[1]
    #print("hiiiiiiiiiiiiiiiiiiiiiiiiii")
    #print(warrior.objects.all())

    context = {
        'user': user,
        'warriors': warriors,
        }
    return render(request, 'game/army.html', context)

def spells(request, spellid):
    #spell = get_object_or_404(Spell, pk = spellid)
    spell = Spell.objects.all()[0]
    spell2 = Spell.objects.all()[1]

    print(spell)

    context = {
        'spell': spell,
        'spell2': spell2,
    }

    return render (request, 'game/spells.html', context)


