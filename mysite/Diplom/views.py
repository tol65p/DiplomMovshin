from django.shortcuts import render, redirect
from . models import Users
from . forms import UserForm, EntryForm

current_user = 'zero'
# Create your views here.
def index(request):
    context = {'current_user': current_user}
    return render(request, 'Diplom/index.html', context=context)

def reg(request):
    global current_user
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            current_user = form.cleaned_data['nickname']
            return redirect('Diplom:runner')
    context = {'form': form}
    return render(request, 'Diplom/reg.html', context=context)

def entry(request):
    global current_user
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            current_user = form.cleaned_data['nickname']
            return redirect('Diplom:index')
    context = {'form': form}
    return render(request, 'Diplom/entry.html', context=context)

def runner(request):
    context = {'current_user': current_user}
    return render(request, 'Diplom/runner.html', context=context)

def event(request):
    return render(request, 'Diplom/event.html')

def RegEvent(request):
    return render(request, 'Diplom/RegEvent.html')

def EnterResults(request):
    return render(request, 'Diplom/EnterResults.html')

def WiewResults(request):
    return render(request, 'Diplom/WiewResults.html')
