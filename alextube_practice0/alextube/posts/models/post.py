from django.db import models
from users.models import Users


class Post(models.Model):

    user = models.ForeignKey(Users)

    video_id = models.CharField(
            max_length=16,
    )

    video_original_title = models.CharField(
            max_length=256,
            blank=True,
            null=True,
    )
    
    title = models.CharField(
            max_length=256,
    )
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_youtube_original_url(self):
        return "https://www.youtube.com/watch?v={video_id}".format(
                video_id=self.video_id,
                )
    youtube_original_url = property(get_youtube_original_url)

    def __str__(self):
        return self.title


