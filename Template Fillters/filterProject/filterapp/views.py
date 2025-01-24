from django.shortcuts import render

# Create your views here.
def example_view(request):
    return render(request, 'template.html', {'name':"world"})

