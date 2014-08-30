from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, max_length=32, db_index=True)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, max_length=32, db_index=True)
    date = models.DateField(auto_now_add=True)
    #num_pics = models.IntegerField(default=0)
    status_choices = (
        ('featured', 'Featured'),
        ('published', 'Published'),
        ('deleted', 'Deleted'),
    )
    status = models.CharField(
        max_length=16, choices=status_choices, default='published')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Post (models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=32, db_index=True)
    date = models.DateField(blank=True, null=True)
    body = models.TextField(max_length=1024, blank=True, null=True)

    STATUS_CHOICES = (
        ('featured', 'Featured'),
        ('published', 'Published'),
        ('deleted', 'Deleted'),
        ('pending', 'Pending'),
        ('flagged', 'Flagged'),
    )

    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, blank=True, null=True)

    views = models.IntegerField(blank=True, null=True)
    # likes = models.IntegerField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'id: %d | hash: %s' % (self.id, self.hash)

