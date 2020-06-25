from django import forms

class ShortForm(forms.Form):
    slug = forms.CharField(label='Slug', max_length=255)
    link = forms.CharField(label='Link', max_length=255)
