from django.db import models


# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=120, unique=True)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    mongo_id = models.CharField(max_length=24, unique=True, null=True,
                                blank=True)

    def __str__(self):
        return self.fullname

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.quote}" - {self.author}'
