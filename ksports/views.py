from django.shortcuts import render_to_response
from django.template import RequestContext
from ksports.models import Person, Message
from ksports.forms import PersonForm
from django.http import HttpResponseRedirect


def getPersons(request):
    Persons = Person.objects.all()
    Persons = [ x for x in Persons if x.inAWeek() ]
    yy = [ x for x in Persons if x.sports.name == 'youyong' ]
    pp = [ x for x in Persons if x.sports.name == 'pingpong' ]
    ym = [ x for x in Persons if x.sports.name == 'yumao' ]
    print yy
    print pp
    print ym
    messages = Message.objects.order_by('-update_time').all()
    if messages:
        message = messages[0]
    else:
        message = None
    return render_to_response('sports.html', 
            {"yy": yy, "pp": pp, "ym": ym, "message": message},
            context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',{},context_instance=RequestContext(request))


def home(request):
    return HttpResponseRedirect('/sports/')


def addPerson(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            sports = data['sports']
            person = Person(name=name, sports=sports)
            person.save()
            return HttpResponseRedirect('/sports/')
    else:
        form = PersonForm()
    return render_to_response('add.html',
            {'form': form},
            context_instance=RequestContext(request))


