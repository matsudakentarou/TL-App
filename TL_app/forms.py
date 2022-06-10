from django import forms

from .models import TLE


class TleForm(forms.ModelForm):
    class Meta:
        model = TLE
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "イベント"}),
	    "year": forms.TextInput(attrs={"class": "form-control", "placeholder": "年代"}),
        }