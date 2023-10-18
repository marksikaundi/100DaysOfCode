# Import necessary modules
from django.http import HttpResponse
from django.shortcuts import render

# Define a view function
def hello(request):
    return HttpResponse("Hello, world!")

# Define a view function that renders a template
def my_view(request):
    context = {'name': 'John'}
    return render(request, 'my_template.html', context)
