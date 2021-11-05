from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(default='post.jpg', upload_to='post_pics')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ('Title: ' + self.title + 'Content: ' + self.content)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # def save(self):
    #     super().save()

    #     img = Image.open(self.picture.path)

    #     if img.height > 350 or img.width > 850:
    #         output_size = (850, 350)
    #         img.thumbnail(output_size)
    #         img.save(self.picture.path)
