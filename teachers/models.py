from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class SubjectCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Subject(models.Model):
    subject_slug = models.SlugField(blank=True, null=True)
    subject_name = models.CharField(max_length=255)
    subject_category = models.ForeignKey(SubjectCategory, on_delete=models.CASCADE, blank=True, null=True)
    subject_subname = models.CharField(max_length=255, blank=True, null=True)
    subject_file_1 = models.FileField(upload_to='subject_files/', blank=True, null=True, verbose_name='Fan dasturi')
    subject_file_2 = models.FileField(upload_to='subject_files/', blank=True, null=True, verbose_name='Uslubiy ko\'rsatma')
    subject_file_3 = models.FileField(upload_to='subject_files/', verbose_name='Fan rejasi')
    subject_bg_pic = models.ImageField(upload_to='subject_files/', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.subject_name, self.subject_category)


class Teacher(models.Model):
    CHOICES = (
        ('Kafedra mudiri', 'Kafedra mudiri'),
        ('Dotsent', 'Dotsent'),
        ('Professor', 'Professor'),
        ('Katta o\'qituvchi', 'Katta o\'qituvchi'),
        ('O\'qituvchi', 'O\'qituvchi'),
        ('Laborant', 'Laborant'),
    )
    CHOICES2 = (
        ('Asosiy shtat', 'Asosiy shtat'),
        ('Ichki o\'rindosh', 'Ichki o\'rindosh'),
        ('Tashqi o\'rindosh', 'Tashqi o\'rindosh'),
    )
    
    teacher_id = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=255, blank=True, null=True, choices=CHOICES)
    type = models.CharField(max_length=255, blank=True, null=True, choices=CHOICES2)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    telegram = models.CharField(max_length=255, default='/')
    instagram = models.CharField(max_length=255, default='/')
    e_dars_url = models.CharField(max_length=255, default='/')
    facebook = models.CharField(max_length=255, default='/')
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    subjects = models.ManyToManyField(Subject)
    teacher_queue=models.IntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.rank, self.type)


class Glossary(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    glossary_slug = models.SlugField(blank=True, null=True)
    glossary_title = models.CharField(max_length=255)
    glossary_body = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.subject, self.glossary_title)

    class Meta:
        ordering = ['glossary_title']


class Book(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255)
    book_pic = models.ImageField(upload_to='resourse/book/')
    book_file = models.FileField(upload_to='resourse/book/')

    def __str__(self):
        return '{} - {}'.format(self.subject, self.book_title)


class WebSite(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    site_title = models.CharField(max_length=255)
    site_url = models.CharField(max_length=255)
    site_intro = models.ImageField(upload_to='site_pic/', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.subject, self.site_title)


class Presentation(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    presentation_title = models.CharField(max_length=255)
    presentation_pic = models.ImageField(upload_to='presentation/', blank=True, null=True)
    presentation_file = models.FileField(upload_to='presentation/')

    def __str__(self):
        return '{} - {}'.format(self.subject, self.presentation_title)


class Maruza(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    maruza_slug = models.CharField(max_length=255, blank=True, null=True)
    maruza_title = models.CharField(max_length=255)
    maruza_file = models.FileField(upload_to='maruzalar/file/')

    def __str__(self):
        return '{} - {}'.format(self.subject, self.maruza_title)


class Test(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = RichTextUploadingField()
    answer = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    timer = models.IntegerField(default=60)

    def __str__(self):
        return '{} - {}'.format(self.subject, self.question)


class Video(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    maruza = models.ForeignKey(Maruza, on_delete=models.CASCADE, blank=True, null=True)
    video_title = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.subject, self.video_title)


class Virtual(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    virtual_title = models.CharField(max_length=255)
    virtual_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.subject, self.virtual_title)


class AmaliyTheme(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    practis_id = models.IntegerField(blank=True, null=True)
    practis_name = models.CharField(max_length=255)
    practis_slug = models.SlugField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.subject, self.practis_name)


class Amaliy(models.Model):
    practis_name = models.ForeignKey(AmaliyTheme, on_delete=models.CASCADE, blank=True, null=True)
    question_slug = models.CharField(max_length=255)
    question_title = models.CharField(max_length=255)
    question = models.TextField()
    solusion = models.TextField(blank=True, null=True)
    checking = models.TextField()
    hint = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.practis_name, self.question_title)


class PortfolioCategory(models.Model):
    portfolio_slug = models.CharField(max_length=255, blank=True)
    portfolio_name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.portfolio_name)


class Portfolio(models.Model):
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_name = models.CharField(max_length=255)
    portfolio_authors = models.TextField()
    portfolio_address = models.TextField()
    portfolio_date = models.DateField()
    portfolio_description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='portfolio_files/', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.teacher, self.portfolio_name)


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    context = models.TextField()
    date = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)


class BestStudent(models.Model):
    name = models.CharField(max_length=255)
    body = RichTextUploadingField()

    def __str__(self):
        return '{}'.format(self.name)


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, default=None, on_delete=models.CASCADE)
    img = models.FileField(upload_to='portfolio_files/')

    def __str__(self):
        return str(self.pk)







