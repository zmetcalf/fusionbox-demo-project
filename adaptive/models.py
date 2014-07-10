import widgy

from widgy.models import Content

from widgy.utils import update_context, render_to_string


@widgy.register
class Adaptive(Content):
    def render(self, context):
        template = 'widgy/adaptive/render.html'
        size = context.get('device_info')

        if size['type'] == 'tablet':
            template = 'widgy/adaptive/tablet.html'
        elif size['type'] == 'phone':
            template = 'widgy/adaptive/phone.html'

        with update_context(context, {'self': self}):
            return render_to_string(template, context)
