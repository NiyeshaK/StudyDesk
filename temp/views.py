from django.shortcuts import render

# Create your views here.
def template(request):
    return render(request ,"templ/index.html")