from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'book_review_title', 'book_rating', 'book_review']
        widgets = {
            'book_review': Textarea(attrs={'cols': 40, 'rows': 15})
        }
