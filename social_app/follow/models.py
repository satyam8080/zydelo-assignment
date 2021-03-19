from django.db import models


# Create your models here.
class Follow(models.Model):
    follow_by = models.IntegerField()
    follow_on = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FollowBy {self.follow_by}, FollowOn {self.follow_on}"
