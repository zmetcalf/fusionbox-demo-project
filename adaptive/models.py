import widgy

from widgy.models import Content

from widgy.utils import update_context, render_to_string

from responsive.context_processors import device_info


@widgy.register
class Adaptive(Content):
    def render(self, context, template=None):
        template = ''
        size = device_info(context)
        if size['device_info']['type'] == 'tablet':
            template = 'widgy/adaptive/tablet.html'
        elif size['device_info']['type'] == 'phone':
            template = 'widgy/adaptive/phone.html'
        else:
            template = 'widgy/adaptive/render.html'

        with update_context(context, {'self': self}):
            return render_to_string(template, context)
