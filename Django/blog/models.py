from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0,'Draft'),(1,'Publish'))

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True)   
    author = models.ForeignKey(to=User,on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS,default=0)


    def __str__(self) :
        return self.title

    #slug is important field that you add to any table that you create in Django.
     # It is the field where URL's are stored i.e what table/app represents what url.
     # If this does not match than frontend never work
     # https://domainname/user --> here user is slug
     # https://domainname/new-blog --> new-blog is slug
