from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase

from .user import add_user, delete_user, get_user, list_user
from .urls import urlpatterns
from .models import NewUser


def create_test_user():
    return get_user_model().objects.create_user(username='TEST_DUDE', email='me@here.com', password='secret')

class ViewTests(SimpleTestCase):
    def test_view_index(self):
        self.check_template('/', 'index.html')
    
    def test_update_user(self):
        self.check_num_user(1)
        a = get_user('thom1664')
        a.name = 'George Orwell'
        a.save()
        self.check_user_name(1, 'George Orwell')
