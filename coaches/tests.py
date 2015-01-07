from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from coaches.models import Coach



class CoachTest(TestCase):

    def test_coach_list(self):
        client = Client()
        coach1 = Coach.objects.create(name="Name", surname="Surname", 
                                      email="test@gmail.com", 
                                      phone="123456", 
                                      coach_type ="Assistant", course_name="Python",
                                      user = User(1))
        response = client.get('/coaches/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Name")

    def test_coach_item(self):
        client = Client()
        coach1 = Coach.objects.create(name="Name", surname="Surname", 
                                      email="test@gmail.com", 
                                      phone="123456", 
                                      coach_type ="Assistant", course_name="Python",
                                      user = User(1))
        response = client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Name")
