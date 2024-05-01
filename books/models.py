from django.db import models

class BookModel(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=255)

    info = models.TextField()
    page = models.IntegerField()
    ebook = models.FileField(upload_to='media/e-books', null = True, blank=True)


    def __str__(self):
        return self.title