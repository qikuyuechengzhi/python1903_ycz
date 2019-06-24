from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TypeWork(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class ProjectName(models.Model):

    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class PartName(models.Model):

    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Summary(models.Model):
    Job_number = models.IntegerField(max_length=10)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    typework = models.ForeignKey(TypeWork,on_delete=models.CASCADE)
    projectname = models.ForeignKey(ProjectName,on_delete=models.CASCADE)
    partname = models.ForeignKey(PartName,on_delete=models.CASCADE)
    amount = models.IntegerField(max_length=5,default=0)
    working = models.IntegerField(max_length=10,default=0)

    def __str__(self):
        return self.username
