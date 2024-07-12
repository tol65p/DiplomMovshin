from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Diplom/index.html')

def reg(request):
    return render(request, 'Diplom/reg.html')