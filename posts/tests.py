from django.test import TestCase
from django.test import SimpleTestCase
from .models import Post
from  django.urls import  reverse


# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self) -> None:
        print("This is initiation")
        Post.objects.create(text="Just a test")
        # This is Setting up a New Object from the Model
        # But it is Not a real data  ;

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_content = f"{post.text}"
        self.assertEqual(expected_object_content, "Just a test")

class HomePageViewTest(TestCase) :
    def setUp(self) -> None:
        pass

    def test_homePage_isOutThere(self):
        # All what we Need Here is To just make Sure Home page exist
        respo = self.client.get('/')
        self.assertEqual(respo , 200)


