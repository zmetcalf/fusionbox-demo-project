import widgy

from widgy.contrib.form_builder.models import FormInput

widgy.unregister(FormInput)

@widgy.register
class BootstrapFormInput(FormInput):

    class Meta:
        proxy = True
        verbose_name = 'Form Input'
        verbose_name_plural = 'Form Inputs'

    @property
    def widget_attrs(self):
        attrs = super(BootstrapFormInput, self).widget_attrs
        attrs['class'] = attrs.get('class', '') + ' form-control'
        return attrs
