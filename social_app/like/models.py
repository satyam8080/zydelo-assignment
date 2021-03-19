from django.db import models


# Create your models here.
class Like(models.Model):
    likeBy = models.IntegerField()
    likeOn = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"LikeBy {self.likeBy}, LikeOn {self.likeOn}"
