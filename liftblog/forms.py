from django import forms

class ContactForm(forms.Form):
    email = forms.CharField(max_length=75)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
