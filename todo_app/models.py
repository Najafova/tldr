from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.category_name)


class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    link = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    # image = models.ImageField(null=True, blank=True)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ('-posted_on', )
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.title)