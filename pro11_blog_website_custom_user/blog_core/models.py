from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# import the settings class to use the "AUTH_USER_MODEL" in the "author" field:
from django.conf import settings


class Blog(models.Model):

    title = models.CharField(max_length=200, blank="True")
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               default=1)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} \
by {self.author.first_name} {self.author.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_user_detail', kwargs={'slug': self.slug})
