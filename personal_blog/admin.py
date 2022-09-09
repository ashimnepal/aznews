from django.contrib import admin
from .models import Category, Contact, NewsLetter, Post, Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(NewsLetter)

