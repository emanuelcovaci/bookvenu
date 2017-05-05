from django.test import TestCase
from django.contrib.auth.models import User
from .forms import LoginForm,UserRegisterForm,AccRegisterForm
# Create your tests here.
class AuthenticationTest(TestCase):
    def accout_setup(self):
        self.user  = User.objects.create_user(username='username',
                                              email = 'email@yahoo.com',
                                              password = 'password123',
                                              first_name = 'First',
                                              last_name = 'Last')

    def test_login(self):
        test_data = {'username':'username','password' : 'password123'}
        form = LoginForm(data=test_data)
        self.assertTrue(form.is_valid())

    def test_bad_user_form(self):
        test_data = {'username':'username123','first_name':'First12','last_name':'Last12',
                    'email':'email@yahoo.com#@$','password':'password', 'retypepassword':'password'}
        form = UserRegisterForm(data=test_data)
        print (form.errors)
        self.assertFalse(form.is_valid())

    def test_good_user_form(self):
        test_data = {'username' : 'username123', 'first_name' : 'FirstName', 'last_name' : 'LastName',
                    'email' : 'email@yahoo.com', 'password':'password123','retypepassword':'password123'}
        form = UserRegisterForm(data=test_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_bad_account_form(self):
        test_data = {'phonenumber' : '1234567890', 'city' : '123', 'country': '123'}
        form = AccRegisterForm(data=test_data)
        print (form.errors)
        self.assertFalse(form.is_valid())

    def test_good_account_form(self):
        test_data = {'phonenumber' : '0733896986', 'city' : 'Timisoara', 'country': 'Timis'}
        form = AccRegisterForm(data=test_data)
        self.assertFalse(form.is_valid())