from django import forms
from django.forms import ModelForm
from . import models

class ContactForm(forms.Form):
    email = forms.CharField(max_length=75)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

class CreateTextPost(ModelForm):
    class Meta:
        model = models.TextPost
        fields = ['title', 'post_image', 'content']

class CreateVideoPost(ModelForm):
    class Meta:
        model = models.VideoPost
        fields = ['title', 'post_video', 'description']

class CreateCarousel(ModelForm):
    class Meta:
        model = models.HomeCarousel
        fields = ['image']

class CreateCarouselText(ModelForm):
    class Meta:
        model = models.HomeCarouselText
        fields = ['text']