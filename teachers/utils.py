import os
import sys

from django.core.files.storage import default_storage
from .models import *
from django.shortcuts import redirect
from slugify import slugify
from PIL import Image, ImageDraw


def maruza_save_items(request):
    items = request.POST
    user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
    if items['status'] != '':
        check_data = Maruza.objects.get(maruza_slug=items['status'])
        if check_data:
            if request.FILES:
                file_obj = request.FILES['file']
                filename = f'maruzalar/file/{file_obj}'
                with default_storage.open(filename, 'wb+') as d:
                    for chunk in file_obj.chunks():
                        d.write(chunk)
            else:
                filename = check_data.maruza_file

            maruza = Maruza.objects.get(maruza_slug=items['status'])
            maruza.maruza_title = items['title']
            maruza.maruza_slug = text_to_slugify(items['title'])
            maruza.maruza_file = filename
            maruza.save()
    else:
        file_obj = request.FILES['file']
        filename = f'maruzalar/file/{file_obj}'
        with default_storage.open(filename, 'wb+') as d:
            for chunk in file_obj.chunks():
                d.write(chunk)

        Maruza.objects.create(
            subject=user,
            maruza_title=items['title'],
            maruza_slug=text_to_slugify(items['title']),
            maruza_file=filename,
        )

    return redirect('maruzalar')


def glossary_save_items(request):
    items = request.POST
    user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
    if items['status'] != '':
        glossary = Glossary.objects.get(glossary_slug=items['status'])
        glossary.glossary_title = items['title']
        glossary.glossary_body = items['body']
        glossary.glossary_slug = text_to_slugify(items['title'])

        glossary.save()
    else:
        Glossary.objects.create(
            subject=user,
            glossary_title=items['title'],
            glossary_body=items['body'],
            glossary_slug=text_to_slugify(items['title']),
        )

    return redirect('glossaries')


def videolar_save_items(request):
    items = request.POST
    user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
    maruza = Maruza.objects.get(maruza_slug=items['maruza_slug'])
    if items['status'] != '':
        video = Video.objects.get(pk=items['status'])
        video.maruza = maruza
        video.video_title = items['title']
        video.video_url = items['url']
        video.save()
    else:
        Video.objects.create(
            subject=user,
            maruza=maruza,
            video_title=items['title'],
            video_url=items['url'],
        )

    return redirect('videolar')


def test_save_items(request):
    items = request.POST
    user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
    if items['status'] != '':
        test = Test.objects.get(pk=items['status'])
        test.question = items['question']
        test.answer = items['answer']
        test.option1 = items['variant1']
        test.option2 = items['variant2']
        test.option3 = items['variant3']
        test.option4 = items['variant4']
        test.save()
    else:
        Test.objects.create(
            subject=user,
            question=items['question'],
            answer=items['answer'],
            option1=items['variant1'],
            option2=items['variant2'],
            option3=items['variant3'],
            option4=items['variant4'],
        )

    return redirect('tests')


def virtual_save_items(request):
    items = request.POST
    user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
    if len(items['status']) != 0:
        check_data = Virtual.objects.get(pk=items['status'])
        if check_data:
            check_data.virtual_title = items['title']
            check_data.virtual_url = items['file']
            check_data.save()
    else:
        Virtual.objects.create(
            subject=user,
            virtual_title=items['title'],
            virtual_url=items['file'],
        )

    return redirect('virtual')


def book_save_items(request):
    items = request.POST
    user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
    if len(items['status']) != 0:
        check_data = Book.objects.get(pk=items['status'])
        if check_data:
            if request.FILES:
                if 'pic' in request.FILES:
                    file_obj = request.FILES['pic']
                    filename = f'resourse/book/{file_obj}'
                    with default_storage.open(filename, 'wb+') as d:
                        for chunk in file_obj.chunks():
                            d.write(chunk)
                else:
                    filename = check_data.book_pic

                if 'file' in request.FILES:
                    file_obj2 = request.FILES['file']
                    filename2 = f'resourse/book/{file_obj2}'
                    with default_storage.open(filename2, 'wb+') as d:
                        for chunk in file_obj2.chunks():
                            d.write(chunk)
                else:
                    filename2 = check_data.book_file
            else:
                filename = check_data.book_pic
                filename2 = check_data.book_file

            check_data.book_title = items['title']
            check_data.book_pic = filename
            check_data.book_file = filename2
            check_data.save()
    else:
        file_obj = request.FILES['pic']
        file_obj2 = request.FILES['file']
        filename = f'resourse/book/{file_obj}'
        filename2 = f'resourse/book/{file_obj2}'
        with default_storage.open(filename, 'wb+') as d:
            for chunk in file_obj.chunks():
                d.write(chunk)
        with default_storage.open(filename2, 'wb+') as d:
            for chunk in file_obj2.chunks():
                d.write(chunk)
        Book.objects.create(
            subject=user,
            book_title=items['title'],
            book_pic=filename,
            book_file=filename2,
        )

    return redirect('book')


def taqdimot_save_items(request):
    items = request.POST
    user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
    if len(items['status']) != 0:
        check_data = Presentation.objects.get(pk=items['status'])
        if check_data:
            if request.FILES:
                if 'pic' in request.FILES:
                    file_obj = request.FILES['pic']
                    filename = f'resourse/taqdimot/{file_obj}'
                    with default_storage.open(filename, 'wb+') as d:
                        for chunk in file_obj.chunks():
                            d.write(chunk)
                else:
                    filename = check_data.presentation_pic
                if 'file' in request.FILES:
                    file_obj2 = request.FILES['file']
                    filename2 = f'resourse/taqdimot/{file_obj2}'
                    with default_storage.open(filename2, 'wb+') as d:
                        for chunk in file_obj2.chunks():
                            d.write(chunk)
                else:
                    filename2 = check_data.presentation_file
            else:
                filename = check_data.presentation_pic
                filename2 = check_data.presentation_file

            check_data.presentation_title = items['title']
            check_data.presentation_pic = filename
            check_data.presentation_file = filename2
            check_data.save()
    else:
        file_obj = request.FILES['pic']
        file_obj2 = request.FILES['file']
        filename = f'resourse/taqdimot/{file_obj}'
        filename2 = f'resourse/taqdimot/{file_obj2}'
        with default_storage.open(filename, 'wb+') as d:
            for chunk in file_obj.chunks():
                d.write(chunk)
        with default_storage.open(filename2, 'wb+') as d:
            for chunk in file_obj2.chunks():
                d.write(chunk)
        Presentation.objects.create(
            subject=user,
            presentation_title=items['title'],
            presentation_pic=filename,
            presentation_file=filename2,
        )

    return redirect('taqdimot')


def amaliy_save_items(request):
    try:
        items = request.POST
        user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
        if len(items) != 5:
            theme = AmaliyTheme.objects.get(practis_slug=request.POST.get('practis_slug'))
            if items['status'] != '':
                amaliy = Amaliy.objects.get(question_slug=items['status'])
                amaliy.question_title = items['title']
                amaliy.question_slug = text_to_slugify(items['title'])
                amaliy.question = items['question']
                amaliy.solusion = items['solusion']
                amaliy.checking = items['checking']
                amaliy.hint = items['hint']
                amaliy.save()
            else:
                Amaliy.objects.create(
                    practis_name=theme,
                    question_title=items['title'],
                    question_slug=text_to_slugify(items['title']),
                    question=items['question'],
                    solusion=items['solusion'],
                    checking=items['checking'],
                    hint=items['hint'],
                )
        else:
            if items['status'] != '':
                amaliy = AmaliyTheme.objects.get(practis_slug=items['status'])
                amaliy.practis_id = items['pract_id']
                amaliy.practis_slug = text_to_slugify(items['title'])
                amaliy.practis_name = items['title']
                amaliy.save()
            else:
                AmaliyTheme.objects.create(
                    subject=user,
                    practis_id=items['pract_id'],
                    practis_slug=text_to_slugify(items['title']),
                    practis_name=items['title']
                )
    except Exception as e:
        print(f'{type(e).__name__}: {e} | Line: {sys.exc_info()[-1].tb_lineno}')

    return redirect('amaliy')


def site_save_items(request):
    items = request.POST
    user = Subject.objects.get(subject_slug=request.POST.get('subject_slug'))
    if len(items['status']) != 0:
        check_data = WebSite.objects.get(pk=items['status'])
        if check_data:
            if request.FILES:
                file_obj = request.FILES['pic']
                filename = f'site_pic/{file_obj}'
                with default_storage.open(filename, 'wb+') as d:
                    for chunk in file_obj.chunks():
                        d.write(chunk)
                crop_site_intro(file_obj)
            else:
                filename = check_data.site_intro

            check_data.site_title = items['title']
            check_data.site_url = items['url']
            check_data.site_intro = filename
            check_data.save()

    else:
        file_obj = request.FILES['pic']
        filename = f'site_pic/{file_obj}'
        with default_storage.open(filename, 'wb+') as d:
            for chunk in file_obj.chunks():
                d.write(chunk)
        crop_site_intro(file_obj)
        WebSite.objects.create(
            subject=user,
            site_title=items['title'],
            site_url=items['url'],
            site_intro=filename
        )

    return redirect('site')


def portfolio_save_items(request):
    items = request.POST
    user = request.user
    images = request.FILES.getlist('file')
    if len(items['status']) != 0:
        check_data = Portfolio.objects.get(pk=items['status'])
        if check_data:
            if request.FILES:
                for img in images:
                    file_obj = img
                    filename = f'portfolio/{file_obj}'
                    with default_storage.open(filename, 'wb+') as d:
                        for chunk in file_obj.chunks():
                            d.write(chunk)
            else:
                filename = check_data.img

            check_data.category = items['category_slug'] if len(items['category_slug']) != 0 else check_data.category
            check_data.portfolio_name = items['title']
            check_data.portfolio_authors = items['authors']
            check_data.portfolio_address = items['address']
            check_data.portfolio_date = items['date']
            check_data.portfolio_description = items['description']
            check_data.img = filename
            check_data.save()

    else:
        for img in images:
            file_obj = img
            filename = f'portfolio/{file_obj}'
            with default_storage.open(filename, 'wb+') as d:
                for chunk in file_obj.chunks():
                    d.write(chunk)

        cat = PortfolioCategory.objects.get(portfolio_slug=items['category_slug'])

        portf = Portfolio.objects.create(
            teacher=user,
            category=cat,
            portfolio_name=items['title'],
            portfolio_authors=items['authors'],
            portfolio_address=items['address'],
            portfolio_date=items['date'],
            portfolio_description=items['description'],
            img=images[0]
        )
        for pic in images[1:]:
            PortfolioImage.objects.create(
                portfolio=portf,
                img=pic
            )

    return redirect('portfolio')


def text_to_slugify(text: str):
    return slugify(text)


def crop_site_intro(img):
    print(os.getcwd())
    filename = f"ATT-KAFEDRA-WEB/media/site_pic/{img}"
    image = Image.open(filename)
    origin_height = 894
    top = 0
    current_height = image.height
    bottom = current_height - origin_height

    cropped_image = image.crop((0, top, image.width, current_height - bottom))

    cropped_image.save(filename)
