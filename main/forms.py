from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['design_rating', 'usability_rating', 'content_rating', 'comment']
