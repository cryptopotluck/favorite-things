from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from random import randint
# Create your models here.
from django.urls import reverse
from django.contrib.auth import get_user_model
# from create import audit
from django.http import HttpResponse
rand_rank = int(randint(1,100))

class Create(models.Model):
    title = models.CharField(max_length=50, blank=False)
    body = models.TextField(blank=True)
    pub_date = models.DateField(default=timezone.now)
    category = models.CharField(blank=True, max_length=200)
    rank = models.IntegerField(blank=True, default=rand_rank)
    metadata = models.TextField(blank=True)
    modified_date = models.DateField(default=timezone.now())
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    metadata_choices = (('Text', 'Text'),
                        ('Number', 'Number'),
                        ('Date', 'Date'),
                        ('Enum', 'Enum'))

    metadata_choice = models.CharField(max_length=50, choices=metadata_choices, default='Text')

    # history = audit.AuditTrail()

    # if rank == HttpResponse:
    #     rank = rank + 1


    def keywords_str( self ):
        tags = Tag.objects.filter( post = self )
        result = ""
        for tag in tags:
            result = result + ", " + tag.tag
        return result


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Tag( models.Model ):
    post = models.ForeignKey(Create, on_delete=models.CASCADE)
    tag = models.CharField(blank = False,max_length=250)
    tag_upper_case = models.CharField(blank = False,max_length=250)##Will be really useful for the search function

    def __str__(self):
        return self.tag