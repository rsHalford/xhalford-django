from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.TextField(db_column='title', blank=True, null=True)
    summary = models.TextField(db_column='summary', blank=True, null=True)
    description = models.TextField(db_column='description', blank=True, null=True)
    technology = models.TextField(db_column='technology', blank=True, null=True)
    #image = models.FilePathField(db_column='image', path='static/portfolio/img/')
    image = models.ImageField(upload_to='media/images/portfolio/', blank=True)
    #pub_date = models.DateTimeField('date published', auto_now_add=True, null=True)
    #slug = models.SlugField(max_length=40, null=False, unique=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'Project'
        app_label = 'portfolio'

#    def save(self, *args, **kwargs):
#        self.image = self.image.replace('static/', '')
#        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
#
#    def get_absolute_url(self):
#        return reverse('project', kwargs={'slug': self.slug})
