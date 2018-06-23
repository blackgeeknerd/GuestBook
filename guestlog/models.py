from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=datetime.now)
    

    def __str__(self):
        return self.name
        #return '<Name: {}, ID: {}>'.format(self.name, self.id)

    # def __unicode__(self):
    #     return 

