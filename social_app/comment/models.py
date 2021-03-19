from django.db import models


# Create your models here.
class Comment(models.Model):
    commentBy = models.IntegerField()
    commentOn = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CommentBy {self.commentBy}, CommentOn {self.commentOn}"
