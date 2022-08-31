from unicodedata import name
from django.urls import path

from .views import (
    DraftListView,
    PostCreateView,
    PostDetailView,
    PostListByCategory,
    PostListByTag,
    PostListView,
    PostUpdateView,
    
    post_delete,
    post_draft_list,
    post_edit,
    post_publish,
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
        "post-publish/<int:pk>/",
        post_publish,
        name="post-publish",
    ),
    path(
        "post-edit/<int:pk>/",
        PostUpdateView.as_view(),
        name="post-edit",
    ),
    path(
        "post-delete/<int:pk>/",
        post_delete,
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
]
