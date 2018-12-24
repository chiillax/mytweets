from django import forms
from .models import Tweet


# class TweetForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea(), max_length=160, help_text='Write here your message!')
#     country = forms.CharField(widget=forms.HiddenInput())

#     def clean(self):
#         cleaned_data = super(TweetForm, self).clean()
#         text = cleaned_data.get('text')
#         if not text:
#             raise forms.ValidationError('You have to write something!')

class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('text', 'country')
