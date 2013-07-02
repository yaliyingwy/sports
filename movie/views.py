#encoding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from movie.models import User, Movie, Comment
from movie.forms import RegisterForm


def listMovie(request):
    movies = Movie.objects.all()
    #split to small lists every 6 movies
    rows = [movies[i:i+6] for i in range(0, len(movies), 6)]
    paginator = Paginator(rows, 2)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('movie_list.html',
            {"contacts": contacts, "page_range": range(1, contacts.paginator.num_pages + 1)},
            context_instance=RequestContext(request))


def showMovie(request, id='1'):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404
    request.session['wy'] = 'ywen'
    return render_to_response('movie_show.html', 
            {'movie': movie},
            context_instance=RequestContext(request))

@csrf_exempt
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        passwd = request.POST['passwd']
        user = User.objects.filter(name=name)[0]
        if user and user.check_passwd(passwd):
            request.session['username'] = name
            request.session.set_expiry(604800)
            return HttpResponse("success")
        else:
            return HttpResponse(u"用户名或密码错误")


def logout(request):
    url = request.META.get('HTTP_REFERER', '/')
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect(url)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            email = data['email']
            passwd = data['passwd']
            person = User(name=name, email=email, passwd=passwd)
            person.save()
            return HttpResponseRedirect('/movie/')
    else:
        form = RegisterForm()
    return render_to_response('register.html',
                  {'form': form},
                  context_instance=RequestContext(request))




