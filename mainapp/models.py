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

    # __str__ method.
    def __str__(self):
        """Simply rendering to the admin view and our templates."""
        return self.title

    def get_absolute_url(self):
        """Canonical URL to post."""
        return reverse('post', args=[str(self.id)])

    
