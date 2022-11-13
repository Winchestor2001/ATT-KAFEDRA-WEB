from django.shortcuts import render,redirect
from teachers.models import *


def home_page(request):
    context = {}
    return render(request, 'kafedra/home.html', context)


def teachers_page(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'kafedra/teachers.html', context)


def edars_page(request):
    edarslar = Subject.objects.all()
    context = {'edarslar': edarslar}
    return render(request, 'kafedra/edars.html', context)


def edars_detail(request, slug):
    edarslar = Subject.objects.get(subject_slug=slug)
    # context = {'edarslar': edarslar}
    return redirect('home',edarslar.subject_slug)


def teacher_portfolio_page(request, pk):
    portfolios = Portfolio.objects.filter(teacher=pk)
    teacher = Teacher.objects.get(teacher_id=pk)
    context = {'portfolios': portfolios, 'teacher': teacher}
    return render(request, 'kafedra/teacher_portfolio.html', context)
