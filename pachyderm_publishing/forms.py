import datetime
from django import forms

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.Password)


class ReviewForm(forms.Form):
    review_date = forms.DateField(initial=datetime.date.today)
    book_review = forms.CharField(widget=forms.Textarea)
