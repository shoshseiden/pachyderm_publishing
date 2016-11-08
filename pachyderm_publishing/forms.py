import datetime
from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField()
    review_date = forms.DateField(initial=datetime.date.today)
    book_review = forms.CharField(widget=forms.Textarea)
