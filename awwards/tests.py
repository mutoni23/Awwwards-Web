from django.test import TestCase
from .models import Project,Rating
from users.models import User,Profile

class ProjectTestClass(TestCase):
    def setUp(self):
        self.user1 = User(username="mutoni23")
        self.user1.save()
        self.project1 = Project(title="delani-studio",description="delani-studio projo",link="mutoni23.github.io/delani-studio/",image="delani-studio",user=self.user1)

    def test_instance(self):
        self.assertTrue(isinstance(self.project1,  Project))

class RatingTestClass(TestCase):
    def setUp(self):
        self.user1 = User(username="mutoni23")
        
        self.user1.save()
        self.project1 = Project(title="delani-studio",description="delani-studio projo",link="mutoni23.github.io/delani-studio/",image="delani-studio",user=self.user1)
        self.project1.save()
        self.new_rating = Rating(design=9,usability=9,content=9,project=self.project1,user=self.user1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_rating,  Rating))