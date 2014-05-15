import widgy

from django import forms

from widgy.contrib.form_builder.models import FormInput

widgy.unregister(FormInput)

@widgy.register
class FormInput(FormInput):
    @property
    def widget(self):
        attrs = {
            'type': self.type,
            'class': 'form-control'
        }
        if self.required:
            attrs['required'] = 'required'

        if self.type == 'date':
            # Use type text because Kalendae doesn't play well with type=date
            attrs['type'] = 'text'
            attrs['class'] += ' date auto-kal'
        return forms.TextInput(attrs=attrs)
