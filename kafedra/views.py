from django.shortcuts import render, redirect, HttpResponse
from teachers.models import *
from django.core import serializers
from itertools import chain
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def home_page(request):
    articles1 = Article.objects.filter(category__name='Yangiliklar')
    articles2 = Article.objects.filter(category__name='Elonlar')
    context = {'articles1': articles1, 'articles2': articles2}
    return render(request, 'kafedra/home.html', context)


def teachers_page(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'kafedra/teachers.html', context)


def edars_page(request):
    edarslar = Subject.objects.all()
    edarslar_list = []
    for item in edarslar:
        #  and AmaliyTheme.objects.filter(subject__subject_slug=item.subject_slug).exists()
        if Maruza.objects.filter(subject__subject_slug=item.subject_slug).exists():
            edarslar_list.append(item)
    context = {'edarslar': edarslar_list}
    return render(request, 'kafedra/edars.html', context)


def edars_detail(request, slug):
    edarslar = Subject.objects.get(subject_slug=slug)
    # context = {'edarslar': edarslar}
    return redirect('home',edarslar.subject_slug)


def teacher_portfolio_page(request, pk):
    portfolios = Portfolio.objects.filter(teacher=pk)
    portfolio_images = PortfolioImage.objects.filter(portfolio__pk=pk)
    teacher = Teacher.objects.get(teacher_id=pk)
    context = {'portfolios': portfolios, 'teacher': teacher, 'portfolio_images': portfolio_images}
    return render(request, 'kafedra/teacher_portfolio.html', context)


def teacher_portfolio_ajax(request):
    portfolios = Portfolio.objects.filter(pk=request.GET['pk'])
    portfolio_images = PortfolioImage.objects.filter(portfolio__pk=int(request.GET['pk']))
    imgs = list(chain(portfolios, portfolio_images))
    data = serializers.serialize('json', imgs)
    return HttpResponse(data, content_type="application/json")


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
            number=request.POST.get('number'),
            context=request.POST.get('context'),
        )
    return render(request, 'kafedra/contact.html')


def best_students_page(request):
    best_students = BestStudent.objects.all()
    context = {'best_students': best_students}
    return render(request, 'kafedra/best_students.html', context)


def error_404_view(request, exception):
    return render(request, 'error_pages/error_404.html')


def article_detail(request, slug):
    user_ip = get_client_ip(request)
    article = Article.objects.get(slug=slug)
    article_type = ArticleCategory.objects.get(id=article.category.id)
    article_gallery = ArticleGallery.objects.filter(article__slug=slug)
    ip_exists = ArticleViewIP.objects.filter(article=article, ip=user_ip).exists()
    if not ip_exists:
        ArticleViewIP.objects.create(
            article=article,
            ip=user_ip
        )
        article.views += 1
        article.save()

    context = {
        'article': article,
        'article_gallery': article_gallery,
        'article_type': article_type,
    }
    return render(request, 'kafedra/article_detail.html', context)


def articles(request, article_type):
    articles = Article.objects.filter(category__name=article_type)
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    context = {
        'articles': paged_articles,
        'article_type': article_type,
    }
    return render(request, 'kafedra/articles.html', context)


