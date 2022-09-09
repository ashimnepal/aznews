from unicodedata import name
from django.urls import path

from personal_blog.models import NewsLetter

from .views import (
    AboutView,
    ContactView,
    DraftListView,
    NewsLetterView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListByCategory,
    PostListByTag,
    PostListView,
    PostUpdateView,   
    SearchPostView,
)

urlpatterns = [
    path(
        "",
        PostListView.as_view(),
        name="post-list",
    ),
    path(
        "post-detail/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail",
    ),
    path(
        "post-create/",
        PostCreateView.as_view(),
        name="post-create",
    ),
    path(
        "post-draft-list/",
        DraftListView.as_view(),
        name="post-draft-list",
    ),
    path(
        "post-edit/<int:pk>/",
        PostUpdateView.as_view(),
        name="post-edit",
    ),
    path(
        "post-delete/<int:pk>/",
        PostDeleteView.as_view(),
        name="post-delete",
    ),
    path(
        "post-list/category/<int:cat_id>/",
        PostListByCategory.as_view(),
        name="post-list-category",
    ),
    path(
        "post-list/tag/<int:tag_id>/",
        PostListByTag.as_view(),
        name="post-list-tag",
    ),
    path(
        "post-search/",
        SearchPostView.as_view(),
        name="post-list-search",
    ),
    path(
        "contact/",
        ContactView.as_view(),
        name="contact",
    ),
    path(
        "about/",
        AboutView.as_view(),
        name="about",
    ),
    path(
        "newsletter/",
        NewsLetterView.as_view(),
        name="about",
    ),


]
