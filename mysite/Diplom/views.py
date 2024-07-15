from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Diplom/index.html')

def reg(request):
    return render(request, 'Diplom/reg.html')

def entry(request):
    return render(request, 'Diplom/entry.html')

def runner(request):
    return render(request, 'Diplom/runner.html')

def RegEvent(request):
    return render(request, 'Diplom/RegEvent.html')

def EnterResults(request):
    return render(request, 'Diplom/EnterResults.html')

def WiewResults(request):
    return render(request, 'Diplom/WiewResults.html')
