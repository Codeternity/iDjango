from django.shortcuts import render

from django.http import HttpResponse


# Create your models here.
def index(request):
    return HttpResponse("Hello, world. You're at the polyv index.")


def player(request):
    testvalue = 'testvalue hello~'
    return render(request, 'polyv/playerdemo.html', {'test': testvalue})
# return HttpResponse("Hello, world. You're at the polyv player.")
