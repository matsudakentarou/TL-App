from django import forms

from .models import TLE


class TleForm(forms.ModelForm):
    class Meta:
        model = TLE
        fields = ('title','year','parent','rank')