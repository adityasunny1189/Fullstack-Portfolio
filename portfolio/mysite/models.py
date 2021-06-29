from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.caption}'

class Project(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(20)])
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title}'

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    excerpt = models.TextField(max_length=200)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title}'

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    author_note = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    institute = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.institute

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.company_name

class Skill(models.Model):
    technology = models.CharField(max_length=100)

    def __str__(self):
        return self.technology
