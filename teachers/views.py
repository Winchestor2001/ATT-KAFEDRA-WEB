from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .utils import *
from django.core import serializers
from html2image import Html2Image


@login_required(login_url='login')
def home_page(request):
    teacher = Teacher.objects.get(teacher_id=request.user)
    context = {'teacher': teacher}
    return render(request, 'teachers/home.html', context)


@login_required(login_url='login')
def maruzalar_page(request):
    if request.POST: return maruza_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    maruzalar = Maruza.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'maruzalar': maruzalar}
    return render(request, 'teachers/maruzalar.html', context)


def delete_maruza(request, slug):
    Maruza.objects.filter(maruza_slug=slug).delete()
    context = {}
    return redirect('maruzalar')


def delete_all_maruza(request):
    Maruza.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('maruzalar')


def edit_maruza(request):
    print(request.GET.get('attr'))
    maruza = Maruza.objects.get(maruza_slug=request.GET.get('attr'))
    data = f"{maruza.maruza_title},{maruza.video},{maruza.maruza_file}"
    return HttpResponse(data)


@login_required(login_url='login')
def glossary_page(request):
    if request.POST: return glossary_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    glossaries = Glossary.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'glossaries': glossaries}
    return render(request, 'teachers/glossary.html', context)


def delete_glossary(request, slug):
    Glossary.objects.filter(glossary_slug=slug).delete()
    return redirect('glossaries')


def delete_all_glossary(request):
    Glossary.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('glossaries')


def edit_glossary(request):
    glossary = Glossary.objects.get(glossary_slug=request.GET.get('attr'))
    data = f"{glossary.glossary_title},{glossary.glossary_body}"
    return HttpResponse(data)


@login_required(login_url='login')
def videolar_page(request):
    if request.POST: return videolar_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    videos = Video.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'videos': videos}
    return render(request, 'teachers/videolar.html', context)


def delete_videolar(request, pk):
    Video.objects.filter(pk=pk).delete()
    return redirect('videolar')


def delete_all_videolar(request):
    Video.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('videolar')


def edit_videolar(request):
    video = Video.objects.get(pk=request.GET.get('attr'))
    data = f"{video.video_title},{video.video_url}"
    return HttpResponse(data)


@login_required(login_url='login')
def test_page(request):
    if request.POST: return test_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    tests = Test.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'tests': tests}
    return render(request, 'teachers/test.html', context)


def delete_test(request, pk):
    Test.objects.filter(pk=pk).delete()
    return redirect('tests')


def delete_all_test(request):
    Test.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('tests')


def edit_test(request):
    test = Test.objects.filter(pk=request.GET.get('attr'))
    data = serializers.serialize('json', test)
    return HttpResponse(data, content_type="application/json")


@login_required(login_url='login')
def virtual_page(request):
    if request.POST: return virtual_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    virtuals = Virtual.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'virtuals': virtuals}
    return render(request, 'teachers/virtual.html', context)


def delete_virtual(request, pk):
    Virtual.objects.filter(pk=pk).delete()
    return redirect('virtual')


def delete_all_virtual(request):
    Virtual.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('virtual')


def edit_virtual(request):
    virtual = Virtual.objects.get(pk=request.GET.get('attr'))
    data = f"{virtual.virtual_title}"
    return HttpResponse(data)


@login_required(login_url='login')
def amaliy_page(request):
    if request.POST: return amaliy_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    amaliy = Amaliy.objects.filter(practis_name__subject__teacher__teacher_id=request.user)
    amaliy_mavzu = AmaliyTheme.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'amaliy': amaliy, 'amaliy_mavzu': amaliy_mavzu}
    return render(request, 'teachers/amaliy.html', context)


def get_amaliy_ajax(request):
    amaliy_questions = AmaliyTheme.objects.filter(subject__subject_slug=request.GET['attr'])
    data = serializers.serialize('json', amaliy_questions)
    return HttpResponse(data, content_type="application/json")


def delete_amaliy(request, slug):
    Amaliy.objects.filter(question_slug=slug).delete()
    return redirect('amaliy')


def delete_all_amaliy(request):
    Amaliy.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('amaliy')


def edit_amaliy(request):
    amaliy = Amaliy.objects.get(pk=request.GET.get('attr'))
    data = serializers.serialize('json', amaliy)
    return HttpResponse(data, content_type="application/json")


@login_required(login_url='login')
def book_page(request):
    if request.POST: return book_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    books = Book.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'books': books}
    return render(request, 'teachers/resourse_book.html', context)


def delete_book(request, pk):
    Book.objects.filter(pk=pk).delete()
    return redirect('book')


def delete_all_book(request):
    Book.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('book')


def edit_book(request):
    book = Book.objects.get(pk=request.GET.get('attr'))
    data = f"{book.book_title}"
    return HttpResponse(data)


@login_required(login_url='login')
def taqdimot_page(request):
    if request.POST: return book_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    presentations = Presentation.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'presentations': presentations}
    return render(request, 'teachers/resourse_taqdimot.html', context)


def delete_taqdimot(request, pk):
    Presentation.objects.filter(pk=pk).delete()
    return redirect('taqdimot')


def delete_all_taqdimot(request):
    Presentation.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('taqdimot')


def edit_taqdimot(request):
    presentation = Presentation.objects.get(pk=request.GET.get('attr'))
    data = serializers.serialize('json', presentation)
    return HttpResponse(data, content_type="application/json")


@login_required(login_url='login')
def site_page(request):
    if request.POST: return site_save_items(request)
    teacher = Teacher.objects.get(teacher_id=request.user)
    sites = WebSite.objects.filter(subject__teacher__teacher_id=request.user)
    context = {'teacher': teacher, 'sites': sites}
    return render(request, 'teachers/resourse_site.html', context)


def delete_site(request, pk):
    WebSite.objects.filter(pk=pk).delete()
    return redirect('site')


def delete_all_site(request):
    WebSite.objects.filter(subject__teacher__teacher_id=request.user).delete()
    return redirect('site')


def edit_site(request):
    site = WebSite.objects.get(pk=request.GET.get('attr'))
    data = serializers.serialize('json', site)
    return HttpResponse(data, content_type="application/json")


def profile_page(request):
    user = User.objects.get(username=request.user)
    teacher = Teacher.objects.get(teacher_id=request.user)
    subject = Subject.objects.filter(teacher__teacher_id=request.user)

    if request.method == 'POST':
        items = request.POST

        user.first_name = items['fio']
        teacher.phone_number = items['number']
        user.email = items['email']
        teacher.telegram = items['tg']
        teacher.instagram = items['inst']
        teacher.facebook = items['fb']

        if request.FILES:
            file_obj = request.FILES['avatar']
            filename = f'subject_logo/{file_obj}_{request.user}'
            with default_storage.open(filename, 'wb+') as d:
                for chunk in file_obj.chunks():
                    d.write(chunk)
            teacher.avatar = filename
        teacher.save()
        user.save()
    context = {'teacher': teacher, 'subject': subject}
    return render(request, 'teachers/profile.html', context)



def login_page(request):
    context = {}
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        usr = authenticate(username=uname, password=pwd)
        if usr:
            login(request, usr)
            return redirect('lk')
        else:
            context['message'] = 'username yoki password xato!!!'
            context['col'] = 'danger'
    return render(request, 'teachers/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')







