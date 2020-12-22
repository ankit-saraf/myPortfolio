from django.db import models

class Introduction(models.Model):
    para1 = models.CharField(default="Intro will come here", max_length=1000)
    para2 = models.CharField(default="Intro will come here", max_length=1000)
    para3 = models.CharField(default="Intro will come here", max_length=1000)
    para4 = models.CharField(default="Intro will come here", max_length=1000)
    para5 = models.CharField(default="Intro will come here", max_length=1000)
    coverImage = models.ImageField(upload_to='images/')
    sideImage = models.ImageField(upload_to='images/')

class TechnicalSkills(models.Model):
    title = models.CharField(default="title", max_length=1000)
    icon = models.ImageField(upload_to='images/')
    rank = models.IntegerField()

    def __str__(self):
        return self.title

class Laf(models.Model):
    title = models.CharField(default="title", max_length=1000)
    desc = models.CharField(default="description will come here", max_length=1000)
    image = models.ImageField(upload_to='images/')
    rank = models.IntegerField()

    def __str__(self):
        return self.title

class Timeline(models.Model):
    title = models.CharField(default="title", max_length=1000)
    desc = models.CharField(default="description will come here", max_length=1000)
    year = models.CharField(default="year", max_length=1000)
    rank = models.IntegerField()
    

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(default="title", max_length=1000)
    desc = models.CharField(default="description will come here", max_length=1000)
    link = models.CharField(default="project_link", max_length=1000)
    image = models.ImageField(upload_to='images/')
    rank = models.IntegerField()

    def __str__(self):
        return self.title