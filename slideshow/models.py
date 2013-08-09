import widgy

from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.file import FilerFileField

from widgy.models import Content

@widgy.register
class Slideshow(Content):
    delay = models.PositiveIntegerField(default=2)
    
    def get_delay_milliseconds(self):
        return self.delay * 1000
        
    def valid_parent_of(self, cls, obj=None):
            return issubclass(cls, Slide)

def SlideField(*args, **kwargs):

    defaults = {
        'null': True,
        'blank': True,
        'verbose_name': _('slide'),
        'related_name': '+',
        'on_delete': models.PROTECT,
    }
    defaults.update(kwargs)

    return FilerFileField(*args, **defaults)

@widgy.register
class Slide(Content):
    editable = True
    
    image = SlideField()
    caption = models.CharField(max_length=255)
    
    @classmethod
    def valid_child_of(cls, parent, obj=None):
        return isinstance(parent, Slideshow)