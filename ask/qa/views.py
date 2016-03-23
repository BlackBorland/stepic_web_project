from django.shortcuts import render

from django.hhtp import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')


