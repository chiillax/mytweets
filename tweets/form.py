from django import forms
from .models import Tweet


class TweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
                           'rows': 1, 'cols': 85, 'class': 'form-control mb-2 mr-sm-2', 'style': 'width: 92%'}), max_length=160)
    country = forms.CharField(widget=forms.HiddenInput())


# class TweetForm(forms.ModelForm):

#     class Meta:
#         model = Tweet
#         fields = ('text', 'country')


class SearchForm(forms.Form):
    query = forms.CharField(label='Enter a keyword to search for',
                            widget=forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'style': 'width: 92%'}))
