from django.test import TestCase
from account.forms import LoginForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

class UserLoginTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        username = 'test_user'
        password = 'test_password'

