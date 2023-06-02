from django import forms
from .models import *


class Forms(forms.ModelForm):
    class Meta:
        model = Bloggers
        fields = "__all__"
