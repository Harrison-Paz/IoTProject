from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Sprinkler, Plan, Log
from .forms import SprinklerForm, SprinklerFormEdit, PlanForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime


@login_required
def home(request):
    return render(request, 'dashboard.html')


@login_required
def view_sprinklers(request):
    sprinklers = Sprinkler.objects.all().order_by('codSprinkler')
    context = {'sprinklers': sprinklers}
    if request.method == 'POST':
        form = SprinklerForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = request.user
            codigo = request.POST.get('codSprinkler')
            current_time = datetime.datetime.now()
            log = Log()
            log.user = usuario
            log.description = "Crear Aspersor ("+ str(codigo) +")"
            log.date = current_time
            log.save()
            return redirect('list_sprinklers')
        else:
            context.update({'form': form})
            return render(request, 'sprinkler/view_sprinklers.html', context)
    return render(request, 'sprinkler/view_sprinklers.html', context)

@login_required
def start_sprinkler(request,id):
    sprinkler = Sprinkler.objects.get(id=id)
    sprinkler.state = True
    sprinkler.save()
    usuario = request.user
    codigo = sprinkler.codSprinkler
    current_time = datetime.datetime.now()
    log = Log()
    log.user = usuario
    log.description = "Encendio Aspersor ("+ str(codigo) +")"
    log.date = current_time
    log.save()
    return redirect('list_sprinklers')

@login_required
def stop_sprinkler(request,id):
    sprinkler = Sprinkler.objects.get(id=id)
    sprinkler.state = False
    sprinkler.save()
    usuario = request.user
    codigo = sprinkler.codSprinkler
    current_time = datetime.datetime.now()
    log = Log()
    log.user = usuario
    log.description = "Apago Aspersor ("+ str(codigo) +")"
    log.date = current_time
    log.save()
    return redirect('list_sprinklers')

@login_required
def edit_sprinkler(request):
    if request.method == 'POST':
        idSprinkler = request.POST.get('id')
        if (idSprinkler != ''):
            sprinkler = Sprinkler.objects.get(id=idSprinkler)
            print("Estado: "+str(sprinkler.state))
            form = SprinklerFormEdit(request.POST, instance=sprinkler)
            if form.is_valid():
                sprinkler = form.save()
                usuario = request.user
                codigo = request.POST.get('codSprinkler')
                current_time = datetime.datetime.now()
                log = Log()
                log.user = usuario
                log.description = "Edito Aspersor ("+ str(codigo) +")"
                log.date = current_time
                log.save()
                return redirect('list_sprinklers')
    return redirect('list_sprinklers')

@login_required
def delete_sprinkler(request, id):
    sprinkler = get_object_or_404(Sprinkler, id=id)
    sprinkler.delete()
    usuario = request.user
    codigo = sprinkler.codSprinkler
    current_time = datetime.datetime.now()
    log = Log()
    log.user = usuario
    log.description = "Crear Aspersor ("+ str(codigo) +")"
    log.date = current_time
    log.save()
    return redirect('list_sprinklers')


# Plan
@login_required
def view_plans(request):
    plans = Plan.objects.all()
    sprinklers = Sprinkler.objects.all().order_by('codSprinkler')
    context = {'sprinklers': sprinklers, 'plans': plans}
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = request.user
            inicio = request.POST.get('startTime')
            fin = request.POST.get('endTime')
            current_time = datetime.datetime.now()
            log = Log()
            log.user = usuario
            log.description = "Creo Plan (hora inicio: "+ str(inicio) +", hora fin: "+ str(fin) +")"
            log.date = current_time
            log.save()
            return redirect('list_plans')
        else:
            context.update({'form': form})
            return render(request, 'plan/view_plans.html', context)
    return render(request, 'plan/view_plans.html', context)

@login_required
def delete_plan(request, id):
    sprinkler = get_object_or_404(Plan, id=id)
    sprinkler.delete()
    usuario = request.user
    inicio = sprinkler.startTime
    fin = sprinkler.endTime
    current_time = datetime.datetime.now()
    log = Log()
    log.user = usuario
    log.description = "Elimino Plan (hora inicio: "+ str(inicio) +", hora fin: "+ str(fin) +")"
    log.date = current_time
    log.save()
    return redirect('list_plans')

@login_required
def view_logs(request):
    log = Log.objects.all().order_by('date').reverse()
    paginator = Paginator(log,10)
    page_number = request.GET.get('page')
    logs = paginator.get_page(page_number)
    context = {'logs': logs}
    return render(request, 'log/view_logs.html', context)