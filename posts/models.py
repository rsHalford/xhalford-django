from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, unique=True, null=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=False)
    categories = models.ManyToManyField('Category', related_name='posts', blank=True)
    text = models.TextField()
    #image = models.FilePathField(path='static/posts/img/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(default=timezone.now, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-published_date']

    #def save(self, *args, **kwargs):
    #    self.image = self.image.replace('static/', '')
    #    super().save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=20)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
