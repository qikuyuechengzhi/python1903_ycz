from django.db import models

# Create your models here.
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_data = models.DateTimeField()

    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    #book作为外键关联到bookinfo表
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    # def skill(self):
    #     return  self.content
    # skill.shor