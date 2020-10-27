from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from base.models import Produto


class ProdotoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('listar_produtos'))
        self.assertRedirects(response, '/?next=/produtos/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('index'))

        # Check our user is logged in

        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        # self.assertTemplateUsed(response, 'catalog/bookinstance_list_borrowed_user.html')
#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get(reverse('listar_produtos'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('listar_produtos'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'produto/listagem.html')
#     def test_pagination_is_ten(self):
#         response = self.client.get(reverse('listar_produtos'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue('is_paginated' in response.context)
#         self.assertTrue(response.context['is_paginated'] == True)
#         self.assertTrue(len(response.context['produtos']) == 10)
#
#
class LoginViewTest(TestCase):

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
#
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login.html')
#
# class IndexViewTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#
#         test_user1 = User.objects.create_user(username='testuser3', password='1X<ISRUkw+tuK')
#         test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
#
#         test_user1.save()
#         test_user2.save()
#     def test_view_url_accessible_by_name(self):
#         # login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_url_exists_at_desired_location(self):
#         # login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get('/index/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         # login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'base/index.html')