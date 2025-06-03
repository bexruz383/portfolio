from django.db import models


class Home(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title


class Portfoliyo(models.Model):
    image = models.ImageField(upload_to='portfoliyo/')
    url = models.URLField()
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.email


class Blog(models.Model):
    image = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=155)
    description = models.TextField()


class Skills(models.Model):
    title = models.CharField(max_length=100)
    parsentage = models.PositiveIntegerField(1)


class Projects(models.Model):
    prject_complate = models.IntegerField()
    years_experience = models.IntegerField()
    happy_clientcs = models.IntegerField()
    customer_rewievs = models.IntegerField()
