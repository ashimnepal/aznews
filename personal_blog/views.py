from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.utils import timezone
from django.views.generic import DetailView, ListView, View, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Category, Post, Tag
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryMixin:
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by("name")
        context["tags"] = Tag.objects.all().order_by("name")
        context["recent_posts"] = Post.objects.filter(status="published").order_by(
            "-created_at"
        )[:5]
        context["top_posts"] = Post.objects.filter(status="published").order_by(
            "-views_count"
        )[:5]
        return context


class PostListView(CategoryMixin, ListView):
    model = Post
    template_name = "News_template/News_list.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(status="published").order_by("-published_at")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["trending_posts"] = Post.objects.all().order_by("-views_count")[:3]
        context["featured_post"] = Post.objects.filter(featured_post=True).order_by("-created_at").first()
        
        return context

        

class DraftListView(CategoryMixin, ListView, LoginRequiredMixin):
    model = Post
    template_name = "blog/post_draft_list.html"
    context_object_name = "drafts"
    queryset = Post.objects.filter(status="unpublished").order_by("-created_at")


class PostListByCategory(View):
    model = Post
    template_name = "blog/post_list.html"

    def get(self, request, cat_id, *args, **kwargs):
        posts = Post.objects.filter(category=cat_id).order_by("published_at")
        categories = Category.objects.all().order_by("name")
        recent_posts = Post.objects.filter(status="published").order_by(
            "-created_at"
        )[:5]
        top_posts = Post.objects.filter(status="published").order_by(
            "-views_count"
        )[:5]
        current_category = Category.objects.get(id=cat_id)

        return render(
            request,
            self.template_name,
            {
                "posts": posts,
                "categories": categories,
                "current_category_id": cat_id,
                "current_category_name": current_category.name,
                "recent_posts":recent_posts,
                "top_posts": top_posts,
            },
        )


class PostListByTag(View):
    model = Post
    template_name = "blog/post_list.html"

    def get(self, request, tag_id, *args, **kwargs):
        posts = Post.objects.filter(tag=tag_id).order_by("published_at")
        categories = Category.objects.all().order_by("name")

        return render(
            request,
            self.template_name,
            {
                "posts": posts,
                "categories": categories,
            },
        )


class PostDetailView(CategoryMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, *args, **kwargs):
        obj = self.get_object()
        obj.views_count += 1
        obj.save()
        return super().get_context_data(*args, **kwargs)



class PostCreateView(CreateView):
    model= Post
    form_class= PostForm
    template_name= "blog/post_create.html"
    success_url= reverse_lazy("post-list")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# def post_create(request):
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.save()
    #     return HttpResponseRedirect("/")
    # else:
    #     form = PostForm()
    #     return render(
    #         request,
    #         "blog/post_create.html",
    #         {"form": form},
    #     )


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return HttpResponseRedirect("/post-draft-list/")
    else:
        form = PostForm(instance=post)
        return render(
            request,
            "blog/post_create.html",
            {"form": form},
        )





class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_edit.html"
    success_url = reverse_lazy("post-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # def get_success_url(self) -> str:
    #     return reverse(post-list)

@login_required
def post_draft_list(request):
    drafts = Post.objects.filter(status = "unpublished").order_by("-created_at")
    return render(
        request,
        "blog/post_draft_list.html",
        {"drafts": drafts},
    )


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published_date = timezone.now()
    post.save()
    return HttpResponseRedirect("/")


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect("/")


class SearchPostView(View):
    template_name="blog/post_list.html"

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            title = request.POST["title"]
            print(title)
            posts = Post.objects.filter(title__icontains = title,)
            categories = Category.objects.all().order_by("name")
            recent_posts = Post.objects.filter(status="published").order_by(
                "-created_at"
            )[:5]
            top_posts = Post.objects.filter(status="published").order_by(
                "-views_count"
            )[:5]
            return render(request, self.template_name, {"posts":posts, "categories":categories, "recent_posts":recent_posts,"top_posts":top_posts})
        

class ContactView(View):
    template_name= "News_template/Contact.html"

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self,request, *args, **kwargs):
       pass

class AboutView(View):
    template_name = "News_template/About.html"

    def get(self,request,*args, **kwargs):
        return render(request, self.template_name)