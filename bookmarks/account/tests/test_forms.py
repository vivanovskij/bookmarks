from django.test import TestCase
from account.forms import LoginForm

class LoginFormTestCase(TestCase):

    def test_username_field_length(self):
        print('Test username lenght...')
        test_username = ''
        for i in range(0, 51):
            test_username += 'a'
        form_data = {'username': test_username, 'password': 'test'}
        form = LoginForm(form_data)
        self.assertFalse(form.is_valid())

