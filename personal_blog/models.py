from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # do not create table for this model


class Tag(TimeStampModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(TimeStampModel):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# write foreign to model which has many relationship
class Post(TimeStampModel):

    STATUS_CHOICES = [
        ("unpublished", "Unpublished"),
        ("published", "Published"),
    ]

    # ("unpublished", "Unpublished")
    # unpublished => inserted in database,
    # Unpublished => display in form

    title = models.CharField(max_length=256)
    featured_image = models.ImageField(
        upload_to="post_images/%Y/%m/%d",
    )
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="unpublished",
    )
    views_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
