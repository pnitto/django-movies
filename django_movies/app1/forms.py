from app1.models import Rating
from django import forms


class RatingForm(forms.ModelForm):


    class Meta:
        exclude = ("user",)
        model = Rating