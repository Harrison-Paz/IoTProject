from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Sprinkler, Plan
from .forms import SprinklerForm, PlanForm


#home

def home(request):
    return render(request, 'dashboard.html')


#sprinkler
def view_sprinklers(request):
    if request.method == 'POST':
        form = SprinklerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_sprinklers')
    sprinklers = Sprinkler.objects.all()
    context = {'sprinklers': sprinklers}
    return render(request, 'sprinkler/view_sprinklers.html', context)


# def edit_sprinkler(request, id):
#     sprinkler = get_object_or_404(Sprinkler, id=id)
#     if request.method == 'POST':
#         form = SprinklerForm(request.POST, instance=sprinkler)
#         if form.is_valid():
#             sprinkler = form.save()
#             return redirect('list_sprinklers')
#     else:
#         form = SprinklerForm(instance=sprinkler)
#     context = {'form': form}
#     return render(request, 'sprinkler/view_Sprinklers.html', context)

def delete_sprinkler(request, id):
    sprinkler = get_object_or_404(Sprinkler, id=id)
    sprinkler.delete()
    return redirect('list_sprinklers')


# Plans

def view_plans(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_plans')
    plans = Plan.objects.all()
    sprinklers = Sprinkler.objects.all()
    context = {'sprinklers': sprinklers, 'plans': plans}
    return render(request, 'plan/view_plans.html', context)


def delete_plan(request, id):
    sprinkler = get_object_or_404(Plan, id=id)
    sprinkler.delete()
    return redirect('list_plans')
