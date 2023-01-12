from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Sprinkler, Plan
from .forms import SprinklerForm, SprinklerFormEdit, PlanForm
from django.contrib import messages


#home

def home(request):
    return render(request, 'dashboard.html')


#sprinkler
def view_sprinklers(request):
    sprinklers = Sprinkler.objects.all()
    context = {'sprinklers': sprinklers}
    if request.method == 'POST':
        form = SprinklerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sprinklers')
        else:
            context.update({'form': form})
            return render(request, 'sprinkler/view_sprinklers.html', context)
    return render(request, 'sprinkler/view_sprinklers.html', context)

def start_sprinkler(request,id):
    sprinkler = Sprinkler.objects.get(id=id)
    sprinkler.state = True
    sprinkler.save()
    return redirect('list_sprinklers')

def stop_sprinkler(request,id):
    sprinkler = Sprinkler.objects.get(id=id)
    sprinkler.state = False
    sprinkler.save()
    return redirect('list_sprinklers')


def edit_sprinkler(request):
    if request.method == 'POST':
        idSprinkler = request.POST.get('id')
        if (idSprinkler != ''):
            sprinkler = Sprinkler.objects.get(id=idSprinkler)
            form = SprinklerFormEdit(request.POST, instance=sprinkler)
            if form.is_valid():
                sprinkler = form.save()
                return redirect('list_sprinklers')
    return redirect('list_sprinklers')

def delete_sprinkler(request, id):
    sprinkler = get_object_or_404(Sprinkler, id=id)
    sprinkler.delete()
    return redirect('list_sprinklers')


# Plans

def view_plans(request):
    plans = Plan.objects.all()
    sprinklers = Sprinkler.objects.all()
    context = {'sprinklers': sprinklers, 'plans': plans}
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_plans')
        else:
            context.update({'form': form})
            return render(request, 'plan/view_plans.html', context)
    return render(request, 'plan/view_plans.html', context)


def delete_plan(request, id):
    sprinkler = get_object_or_404(Plan, id=id)
    sprinkler.delete()
    return redirect('list_plans')
