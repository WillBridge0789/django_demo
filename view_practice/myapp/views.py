from django.shortcuts import render
# imported the class HttpResponse from django.http module
from django.http import HttpResponse
# imported Python's datetime library 
import datetime

# defined a function that will be the view function (current_datetime())
# Each view function takes an HttpRequest object as its 1st parameter. Typically named "request"
# Name of the view function doesn't matter and it doesn't have to be named a certain way. 
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    # This view returns an HttpResponse object that contains the generated response.
    return HttpResponse(html)

def say_hello(request):
    greeting = 'Hi everyone!'
    return HttpResponse(greeting)

