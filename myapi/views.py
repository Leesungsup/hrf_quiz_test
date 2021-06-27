from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    html="<html><body>Hi</body></html>"
    return HttpResponse(html)