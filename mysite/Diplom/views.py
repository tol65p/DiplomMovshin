from django.shortcuts import render, redirect
from . models import Users, Runners
from . forms import UserForm, EntryForm, RunnerForm

current_user = 'zero'
current_user_rec = None
# Create your views here.
def index(request):
    context = {'current_user': current_user}
    return render(request, 'Diplom/index.html', context=context)

def reg(request):
    global current_user, current_user_rec
    if request.method != 'POST':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            current_user = form.cleaned_data['nickname']
            current_user_rec = Users.objects.filter(nickname=current_user)[0]
            return redirect('Diplom:runner')
    context = {'form': form}
    return render(request, 'Diplom/reg.html', context=context)

def entry(request):
    global current_user, current_user_rec
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            current_user = form.cleaned_data['nickname']
            current_user_rec = Users.objects.filter(nickname=current_user)[0]
            return redirect('Diplom:index')
    context = {'form': form}
    return render(request, 'Diplom/entry.html', context=context)

def exit(request):
    global current_user, current_user_rec
    current_user = 'zero'
    current_user_rec = None
    return redirect('Diplom:index')
def runner(request):
    if Runners.objects.filter(user=current_user_rec).exists():
        runner_rec = Runners.objects.get(user=current_user_rec)
    else:
        runner_rec = None
    if request.method != 'POST':
        form = RunnerForm(instance=runner_rec)
    else:
        form = RunnerForm(request.POST, instance=runner_rec)
        if form.is_valid():
            if not runner_rec:
                new_runner = form.save(commit=False)
                new_runner.user = current_user_rec
                new_runner.save()
            else:
                form.save()
            return redirect('Diplom:index')
    context = {'current_user': current_user, 'form': form}
    return render(request, 'Diplom/runner.html', context=context)

def event(request):
    return render(request, 'Diplom/event.html')

def RegEvent(request):
    return render(request, 'Diplom/RegEvent.html')

def EnterResults(request):
    return render(request, 'Diplom/EnterResults.html')

def WiewResults(request):
    return render(request, 'Diplom/WiewResults.html')
