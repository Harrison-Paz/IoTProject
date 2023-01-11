from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Sprinkler, Plan
from .forms import SprinklerForm, PlanForm


#home

def home(request):
    return render(request, 'dashboard.html')


#sprinkler

def create_sprinkler(request):
    if request.method == 'POST':
        form = SprinklerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_sprinklers')
    else:
        form = SprinklerForm()
    context = {'form': form}
    return render(request, 'create_sprinkler.html', context)

def view_sprinklers(request):
    sprinklers = Sprinkler.objects.all()
    context = {'spriklers': sprinklers}
    return render(request, 'sprinkler/view_sprinklers.html', context)


def edit_sprinkler(request, sprinkler_id):
    sprinkler = get_object_or_404(Sprinkler, id=sprinkler_id)
    if request.method == 'POST':
        form = SprinklerForm(request.POST, instance=sprinkler)
        if form.is_valid():
            sprinkler = form.save()
            return redirect('view_sprinklers')
    else:
        form = SprinklerForm(instance=sprinkler)
    context = {'form': form}
    return render(request, 'edit_sprinkler.html', context)

def delete_sprinkler(request, sprinkler_id):
    sprinkler = get_object_or_404(Sprinkler, id=sprinkler_id)
    sprinkler.delete()
    return redirect('view_sprinklers')


# Plans
def view_plans(request):
    plans = Plan.objects.all()
    return render(request, 'plan/view_plans.html', {'plans': plans})
