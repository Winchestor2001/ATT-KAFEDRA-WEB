from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from teachers.models import User


class ArticleCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Article(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    context = RichTextUploadingField()
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.category, self.title)

    class Meta:
        ordering = ['-created_date']


class ArticleViewIP(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class ArticleGallery(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return str(self.article)


class KafedraHistory(models.Model):
    context = RichTextUploadingField()

    def __str__(self):
        return "Kafedra tarixi"


class IqdidorliStudents(models.Model):
    context = RichTextUploadingField()

    def __str__(self):
        return "Iqdidorli Talabalar"

