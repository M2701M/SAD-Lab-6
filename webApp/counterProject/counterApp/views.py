from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Counter
from django.db.models import F


# Create your views here.
def button(request):
    template = loader.get_template('button.html')
    rendered = template.render()
    if Counter.objects.first() is None:
        counter = Counter()
        counter.save()
    else:
        counter = Counter.objects.first()
    manipulated = rendered.replace("!unique!", f"{counter.value}")  # don't judge me please
    return HttpResponse(manipulated)


def addCounter(request):
    counter = Counter.objects.first()
    counter.value += 1
    counter.save()
    return HttpResponse(counter.value)


def resetCounter(request):
    counter = Counter.objects.first()
    counter.value = 0
    counter.save()
    return HttpResponse(counter.value)
