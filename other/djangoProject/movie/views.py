from django.shortcuts import render, HttpResponse

# Create your views here.
def movie_list(request):
    return HttpResponse("电影列表")

def movie_detail(request, movie_id):
    return HttpResponse(f"电影id是：{movie_id}")


def index(request):
    class Actor:
        def __init__(self, name):
            self.name = name

    time = {
        'first' : "2000-01-02",
        'second': "2002-02-03"
    }
    context = {
        "name" : 'hongzhu',
        "time" : time,
        "actor" : Actor("stan"),
        'html' : "<div><h1>nihao</h1></div>"
    }
    return render(request, 'index2.html', context = context)