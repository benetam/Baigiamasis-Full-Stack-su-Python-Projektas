from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import ImageTk

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Post(models.Model):
    choices = Category.objects.all().values_list('name', 'name')
    choice_list = []
    for item in choices:
        choice_list.append(item)

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='',upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


