from django.contrib import admin

from widgy.admin import WidgyAdmin

from test_form.models import TestModel


admin.site.register(TestModel, WidgyAdmin)
