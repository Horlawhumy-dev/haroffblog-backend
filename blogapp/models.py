from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify


class BlogCategory(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField()
    date_created = models.DateTimeField(blank=True, default=datetime.now())

    def save(self, *args, **kwargs):
        original_slug = slugify(self.category)
        queryset = BlogCategory.objects.all().filter(slug__iexact=original_slug).count()
        count = 1
        postSlug = original_slug
        while(queryset):
            postSlug = original_slug.lower() + '-' + str(count)
            count = count + 1
            queryset = BlogCategory.objects.all().filter(slug__iexact=postSlug).count()

        self.slug = postSlug
        super(BlogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.category


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey(BlogCategory, null=True, on_delete=models.SET_NULL)
    excerpt = models.CharField(max_length=500)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    year = models.IntegerField()
    month = models.CharField(max_length=10)
    day = models.IntegerField()
    featured = models.BooleanField(default=False)
    recent = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now(), blank=True)


    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()
        count = 1
        postSlug = original_slug
        while(queryset):
            postSlug = original_slug.lower() + '-' + str(count)
            count = count + 1
            queryset = BlogPost.objects.all().filter(slug__iexact=postSlug).count()

        self.slug = postSlug

        if self.featured:
            try:
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

