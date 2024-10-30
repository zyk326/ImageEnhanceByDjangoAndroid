from email.header import Header

from django.shortcuts import HttpResponse, render
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)
        print(request.COOKIES)
        return HttpResponse('OK')

def add_cookie(request):
    response = HttpResponse('set cookies')
    max_age = 60 * 60 * 24 * 7
    response.set_cookie('username', 'zyk', max_age=max_age)
    return response

def del_cookie(request):
    response = HttpResponse('delete cookies')
    response.delete_cookie('username')
    return response

def add_ses(request):
    request.session['username'] = 'zyk'
    return HttpResponse('set cookies')

def get_ses(request):
    username = request.session.get('username')
    print(username)
    return HttpResponse('get cookies' + username)