# from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
# from django.contrib.auth import get_user_model
# from .views import (RegisterView, ActivationView, ForgotPasswordView, ForgotPasswordCompleteView, BecomeEmployerView,
#                     BecomeEmployerCompleteView, DeleteUserView)
#
#
# class AuthTest(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.user = get_user_model().objects.create_user(
#             email='testuser@gmail.com',
#             password='12345678',
#             is_active=True,
#             activation_code='1234'
#         )
#
#     def test_registration(self):
#         data = {
#             'email': 'new_testuser@gmail.com',
#             'password': '12345678',
#             'password_confirm': '12345678',
#             'first_name': 'Test',
#             'last_name': 'Testtt'
#         }
#         request = self.factory.post('api/v1/account/register/', data, format='json')
#         # print(request)
#         # print('==================================')
#         view = RegisterView.as_view()
#         response = view(request)
#         # print(response.status_code)
#         # print('-----------------------------------')
#         # assert response.status_code == 201
#         assert get_user_model().objects.filter(email=data['email']).exists
#
#     def test_login(self):
#         data = {
#             'email': 'testuser@gmail.com',
#             'password': '12345678'
#         }
#         request = self.factory.post('api/v1/account/login/', data, format='json')
#         force_authenticate(request, user=self.user)
#         view = ActivationView.as_view()
#         response = view(request)
#         # print(response.status_code)
#         # print('-------------------------')
#         # assert response.status_code == 200
#         assert 'access' in response.data
#
#     def test_forgot_password(self):
#         # force_authenticate(request, )
#         data = {'email': 'testuser@gmail.com'}
#         request = self.factory.post('api/v1/account/forgot_password/', data, format='json')
#         view = ForgotPasswordView.as_view()
#         response = view(request)
#         # print(response, response.data)
#         assert response.status_code == 200
#
#     def test_forgot_password_complete(self):
#         data = {
#             'email': 'testuser@gmail.com',
#             'activation_code': '1234',
#             'new_password': '123456789',
#             'new_password_confirm': '123456789'
#         }
#         request = self.factory.post('api/v1/account/forgot_password_complete/', data)
#         view = ForgotPasswordCompleteView.as_view()
#         response = view(request)
#         print(response, response.data)
#         # assert response.status_code == 200
#         self.assertEqual(response.status_code, 200)
#
#     def become_employer(self):
#         self.become_employer()
#         data = {
#             'email': 'testuser@gmail.com',
#             'password': '12345'
#         }
#         request = self.factory.post('api/v1/account/become_employer/', data)
#         view = BecomeEmployerView.as_view()
#         response = view(request)
#         print('==========================================')
#         print(response, response.data)
#         print('==========================================')
#         self.assertEqual(response.status_code, 200)
