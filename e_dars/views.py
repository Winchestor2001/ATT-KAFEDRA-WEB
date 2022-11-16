from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm, SignInForm
from teachers.models import *
from .serializers import QuizesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from html2image import Html2Image


def home_page(request, slug):
    users = User.objects.all().count()
    resources = Book.objects.filter(subject__subject_slug=slug)
    glossaries = Glossary.objects.filter(subject__subject_slug=slug)
    practis_themes = AmaliyTheme.objects.filter(subject__subject_slug=slug).count()
    themes = Maruza.objects.filter(subject__subject_slug=slug).count()
    # posts = Post.objects.all()
    videos = Video.objects.filter(subject__subject_slug=slug).count()
    subject = Subject.objects.get(subject_slug=slug)
    context = {
        'users': users,
        'books': resources,
        'glossaries': glossaries[:3],
        'practis_themes': practis_themes,
        'themes': themes,
        'videos': videos,
        # 'posts': posts,
        'subject': subject,
    }
    return render(request, 'e_dars/home.html', context)


def themes_page(request, slug):
    theme = Maruza.objects.filter(subject__subject_slug=slug)
    subject = Subject.objects.get(subject_slug=slug)
    context = {'themes': theme, 'subject': subject,}
    return render(request, 'e_dars/themes_page.html', context)


def theme_detail(request, slug1, slug):
    theme = get_object_or_404(Maruza, maruza_slug=slug)
    subject = Subject.objects.get(subject_slug=slug1)
    context = {'theme': theme, 'subject':subject}
    return render(request, 'e_dars/theme_detail.html', context)


def practis_themes_page(request, slug):
    practis_theme = AmaliyTheme.objects.filter(subject__subject_slug=slug).order_by('practis_id')
    subject = Subject.objects.get(subject_slug=slug)
    context = {'practis_theme': practis_theme, 'subject': subject}
    return render(request, 'e_dars/practis_theme.html', context)


def practis_page(request, slug1, slug):
    practis = Amaliy.objects.filter(practis_name__practis_slug=slug)
    subject = Subject.objects.get(subject_slug=slug1)
    practis_theme = [item.question_title for item in practis]
    context = {'practis': practis, 'practis_theme': practis_theme[0], 'subject': subject}
    return render(request, 'e_dars/practis_page.html', context)


def quiz_page(request, slug):
    subject = Subject.objects.get(subject_slug=slug)
    context = {'subject': subject}
    if request.user.is_authenticated:
        return render(request, 'e_dars/quiz_page.html', context)
    else:
        return redirect('sign_in', slug=slug)


# def posts_page(request):
    # posts = Post.objects.all()
    # context = {'posts': posts}
    # return render(request, 'e_dars/posts.html', context)


# def posts_detail(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     post_viwe = post.post_views + 1
#     post.post_views = post_viwe
#     post.save()
#     context = {'post': post}
#     return render(request, 'e_dars/post_detail.html', context)


def resources_page(request, slug):
    hti = Html2Image()
    # resources = Resource.objects.all()
    books = Book.objects.filter(subject__subject_slug=slug)
    exposures = Presentation.objects.filter(subject__subject_slug=slug)
    useful_links = WebSite.objects.filter(subject__subject_slug=slug)
    subject = Subject.objects.get(subject_slug=slug)
    resources_with_link = []
    for useful_link in useful_links:
        if len(str(useful_link.site_intro)) <= 0:
            resources_with_link.append({'id': useful_link.pk, 'link': useful_link.site_url, 'name': useful_link.site_title})
            for site in resources_with_link:
                site_name = site['name']
                save_pic_path = f'site_pic/{site_name}.png'
                hti.output_path = 'media/site_pic/'
                hti.screenshot(url=site['link'], save_as=f"{site_name}.png")
                res = get_object_or_404(WebSite, id=site['id'])
                res.site_intro = save_pic_path
                res.save()
                print('screen')

    context = {'books': books, 'exposures': exposures, 'useful_links': useful_links, 'subject': subject}
    return render(request, 'e_dars/resources_page.html', context)


def glossary_page(request, slug):
    glossaries = Glossary.objects.filter(subject__subject_slug=slug)
    subject = Subject.objects.get(subject_slug=slug)
    context = {'glossaries': glossaries, 'subject': subject}
    return render(request, 'e_dars/glossary_page.html', context)


def sign_up(request, slug):
    subject = Subject.objects.get(subject_slug=slug)
    context = {'subject': subject}
    if request.method == 'POST':
        ism = request.POST['ism']
        familya = request.POST['familya']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        usr = User.objects.filter(username=username)
        if len(username) < 6:
            context['message'] = 'Username kamida 6 ta belgi bolsin!'
            context['col'] = 'danger'
        elif len(password) < 8:
            context['message'] = 'Password kamida 8 ta belgi  bolsin!'
            context['col'] = 'danger'
        elif password != password2:
            context['message'] = 'Passwordlar mos kelmadi!'
            context['col'] = 'danger'
        elif usr:
            context['message'] = 'Bu foydalanuvchi avval royxatdan otgan'
            context['col'] = 'danger'
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = ism
            user.last_name = familya
            user.save()
            return redirect('sign_in', slug=slug)
    return render(request, 'e_dars/sign_up.html', context)


def sign_in(request, slug):
    subject = Subject.objects.get(subject_slug=slug)
    context = {'subject': subject}
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        usr = authenticate(username=uname, password=pwd)
        if usr:
            login(request, usr)
            return redirect('home', slug=slug)
        else:
            context['message'] = 'username yoki password xato!!!'
            context['col'] = 'danger'
    return render(request, 'e_dars/sign_in.html', context)


def logout_user(request, slug):
    print(slug)
    logout(request)
    return redirect('home',slug=slug)


def video_page(request, slug):
    videos = Video.objects.filter(subject__subject_slug=slug)
    subject = Subject.objects.get(subject_slug=slug)
    context = {'videos': videos, 'subject': subject}
    return render(request, 'e_dars/videos_page.html', context)


@api_view(['GET'])
def quiz_api(request, slug):
    quizes = Test.objects.filter(subject__subject_slug=slug)
    serializer = QuizesSerializer(quizes, many=True)
    return Response(serializer.data)


def pdf_page(request):
    return render(request, 'e_dars/pdf.html')

