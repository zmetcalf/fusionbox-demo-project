import widgy

from django.db import models

from widgy.models import Content

@widgy.register
class Slideshow(Content):
    delay = models.PositiveIntegerField(default=2)
    
    def get_delay_milliseconds(self):
        return self.delay * 1000
        
    def valid_parent_of(self, cls, obj=None):
            return issubclass(cls, Slide)
    
@widgy.register
class Slide(Content):
    image = models.ImageField(upload_to='slides/', null=True)
    caption = models.CharField(max_length=255)
    
    @classmethod
    def valid_child_of(cls, parent, obj=None):
        return isinstance(parent, Slideshow)
        