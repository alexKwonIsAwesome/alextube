from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post


class PostModelTest(TestCase):

    def setUp(self):
      
        self.user = get_user_model().objects.create_user(
                username="test_username",
                password="test_password",
        )

        self.post_video_id = "alextube"

        self.post = self.user.post_set.create(
                video_id = self.post_video_id,
                title = "test_title",
        )
    
    def test_post_model_should_have_youtube_original_url(self):

        """
        The Post model should be able to create youtube original url
        with the given youtube hash form video_id
        """
        self.assertEqual(
                self.post.get_youtube_original_url(),
                "https://www.youtube.com/watch?v={post_video_id}".format(
                    post_video_id=self.post_video_id,
                ),
        )


