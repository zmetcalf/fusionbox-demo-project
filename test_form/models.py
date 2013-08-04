from django.db import models

class TestModel(models.Model):
    
    def __unicode__(self):
        return self.title
    
    title = models.CharField(max_length=200)
    test_string = models.TextField()