from __future__ import absolute_import

from widgy.contrib.review_queue.site import ReviewedWidgySite

# TODO - Make this a productive part of the site - copied from Demo
class FusionboxDemoProject(ReviewedWidgySite):
    def valid_parent_of(self, parent, child_class, obj=None):
        from widgy.contrib.widgy_i18n.models import I18NLayout
        if isinstance(parent, I18NLayout):
            return True
        else:
            return super(FusionboxDemoProject, self).valid_parent_of(parent,\
                        child_class, obj)

widgy_site = FusionboxDemoProject()