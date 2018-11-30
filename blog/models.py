from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(Timestamp):
    title = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=50)
    image = models.ImageField(default=None, blank=True)
    favorited_by = models.ManyToManyField(User, through='Favorite', related_name='favorite_posts')
    upvoted = models.ManyToManyField(User, through='Vote', related_name='voted')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "posts/%s/" % self.slug

class Comment(Timestamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="comments")
    comment = models.CharField(max_length=400)

    def __str__(self):
        return self.comment

def get_image_path(instance, filename):
    return '/'.join(['post_images', instance.post.slug, filename])

class Favorite(Timestamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="favorites")

class Vote(Timestamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="votes")

# class Upload(Timestamp):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="uploads")
#     image = models.ImageField(upload_to=get_image_path)
