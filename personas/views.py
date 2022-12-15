from django.shortcuts import render

# Create your views here.
def helloword(request):
    return render(request, 'Index.html')