from tkinter import Widget
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Contact, NewsLetter, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("category","tag","title", "content","featured_image","status" )





        widgets= {"content" : SummernoteWidget(),}



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'