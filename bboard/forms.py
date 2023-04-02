from django.forms import ModelForm

from django.apps import apps

from bboard.models import Bb


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ['title', 'content', 'price', 'rubric']
