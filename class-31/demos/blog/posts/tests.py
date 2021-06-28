from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1,
            title="Green Eggs and Ham",
            body="I do not like green eggs and ham, Sam I am.",
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = post.title
        actual_body = post.body

        expected_author = "testuser1"
        expected_title = "Green Eggs and Ham"
        expected_body = "I do not like green eggs and ham, Sam I am."

        self.assertEqual(actual_author, expected_author)
        self.assertEqual(actual_title, expected_title)
        self.assertEqual(actual_body, expected_body)
