from django.db import models
from django.conf import settings
from django.urls import reverse

class BlogPost(models.Model):
    """Class for blog posts."""
    title = models.CharField(max_length=200, unique=True)

    # Add a foreign key.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    
    # Body field.
    body = models.TextField()

    # The post date.
    postdate = models.DateTimeField(auto_now_add=True,blank=True)


     # Many to many relationship model for BlogPosts and Tags.
    tags = models.ManyToManyField("Tag", related_name="posts")

    # __str__ method.
    def __str__(self):
        """Simply rendering to the admin view and our templates."""
        return self.title

    def get_absolute_url(self):
        """Canonical URL to post."""
        return reverse('post', args=[str(self.id)])

    
class Tag(models.Model):
    """A class for post tags."""

    # Tag names must be 50 chars or less and unique.
    name = models.CharField(max_length=50, unique=True)

    # Method to sanitize input.
    def clean(self):
        self.name = self.name.lower()

    # Make tags readable.
    def __str__(self) -> str:
        return self.name


    def get_absolute_url(self):
        return reverse('tag_posts', args=[str(self.name)])

