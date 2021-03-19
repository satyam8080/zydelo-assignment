from django.db import models


# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=999)
    user = models.IntegerField()
    post_image = models.ImageField(default='noimg.jpg', upload_to='posts_images')
    likes_count = models.IntegerField(default=0, blank=True)
    comments_count = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post_id: {self.post}, Likes: {self.likes_count}"
