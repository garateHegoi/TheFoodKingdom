from django.conf import settings
from django.forms import ModelForm, DateField

from .models import Txartelak


class DataForm(ModelForm):
    iraungitze_data = DateField(input_formats=settings.DATE_FORMAT)

    class Meta:
        model = Txartelak
