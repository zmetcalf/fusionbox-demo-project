from django.views.generic import DetailView

from widgy.contrib.form_builder.views import HandleFormMixin

from test_form.models import TestModel

class TestView(DetailView, HandleFormMixin):
    model = TestModel

    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        return super(EventDetailView, self).post(*args, **kwargs)