import unittest
from nucleus.models import Author, BlogPost


class TestAuthor(unittest.TestCase):
    """Lame tests for nucleus.models.Author
    """
    def setUp(self):
        self.author = Author.objects.create(
            name="John Doe", avatar_url="http://avatars.com/johndoe.jpeg",
            bio="Something about John Doe!"
        )

    def test_author_save(self):

        _author = Author.objects.get(id=self.author.id)

        self.assertEqual(_author.name, "John Doe")
        self.assertEqual(_author.avatar_url, "http://avatars.com/johndoe.jpeg")
        self.assertEqual(_author.bio, "Something about John Doe!")

    def tearDown(self):
        self.author.delete()


class TestBlogPost(unittest.TestCase):
    """Lame tests for nucleus.models.BlogPost
    """
    def setUp(self):
        self.author = Author.objects.create(
            name="John Doe", avatar_url="http://avatars.com/johndoe.jpeg",
            bio="Something about John Doe!"
        )
        self.blog = BlogPost.objects.create(
            title="First Blog", content="Blog Content", author=self.author
        )

    def test_blogpost_save(self):

        _blog = BlogPost.objects.get(id=self.blog.id)

        self.assertEqual(_blog.title, "First Blog")
        self.assertEqual(_blog.content, "Blog Content")
        self.assertEqual(_blog.author_id, self.author.id)

    def tearDown(self):
        self.author.delete()
        self.blog.delete()
