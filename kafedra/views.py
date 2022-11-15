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


def subjects_page(request):
    subject1 = Subject.objects.filter(subject_category__category='AXBOROT TIZIMLARI VA TEXNOLOGIYALARI')
    subject2 = Subject.objects.filter(subject_category__category='INFORMATIKA VA AXBOROT TEXNOLOGIYALARI')
    subject3 = Subject.objects.filter(subject_category__category='TEXNOLOGIK JARAYONLARNI BOSHQARISHNING AXBOROT KOMMUNIKATSIYA TIZIMLARI')
    context = {'subject1': subject1, 'subject2': subject2, 'subject3': subject3}
    return render(request, 'kafedra/subjects.html', context)


def tarixi_page(request):
    context = {}
    return render(request, 'kafedra/tarix.html', context)


def contact_page(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            context=request.POST.get('context'),
        )
    return render(request, 'kafedra/contact.html')


def best_students_page(request):
    best_students = BestStudent.objects.all()
    context = {'best_students': best_students}
    return render(request, 'kafedra/best_students.html', context)
