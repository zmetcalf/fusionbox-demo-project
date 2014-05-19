import widgy

from widgy.contrib.form_builder.models import FormInput

widgy.unregister(FormInput)

@widgy.register
class FormInput(FormInput):

    class Meta:
        proxy = True

    @property
    def widget_input_class(self):
        return 'form-control'
