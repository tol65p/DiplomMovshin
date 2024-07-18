from django.shortcuts import render, redirect
from . models import Users
from . forms import UsersForm

# Create your views here.
def index(request):
    return render(request, 'Diplom/index.html')

def reg(request):
    if request.method != 'POST':
        form = UsersForm()
    else:
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Diplom:runner')
    context = {'form': form}
    return render(request, 'Diplom/reg.html', context=context)

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
