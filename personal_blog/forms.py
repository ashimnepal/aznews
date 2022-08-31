from tkinter import Widget
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("category","tag","title", "content","featured_image","status" )





        widgets= {"content" : SummernoteWidget(),}
