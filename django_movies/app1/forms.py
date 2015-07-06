from django import forms


class RatingForm(forms.Form):
    rater = forms.IntegerField()
