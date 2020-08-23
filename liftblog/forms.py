from django import forms
from django.db import models
from django.forms import ModelForm
from .models import TextPost, VideoPost, HomeCarousel, HomeCarouselText

class ContactForm(forms.Form):
    email = forms.CharField(max_length=75)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

class CreateTextPost(ModelForm):
    class Meta:
        model = TextPost
        fields = ['title', 'post_image', 'content']

class CreateVideoPost(ModelForm):
    class Meta:
        model = VideoPost
        fields = ['title', 'post_video', 'description']

class CreateCarousel(ModelForm):
    class Meta:
        model = HomeCarousel
        fields = ['image']

class CreateCarouselText(ModelForm):
    class Meta:
        model = HomeCarouselText
        fields = ['text']