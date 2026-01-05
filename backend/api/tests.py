from django.test import TestCase
from .models import RifUser
from .serializers import UserSerializer

class UserSerializerTest(TestCase):
    def test_create_user_with_is_staff(self):
        data = {
            'username': 'staffuser',
            'email': 'staff@example.com',
            'password': 'securepassword',
            'is_staff': True
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()

        self.assertTrue(user.is_staff)
        self.assertTrue(user.check_password('securepassword'))
        self.assertEqual(user.username, 'staffuser')
