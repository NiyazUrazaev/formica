from django.shortcuts import render
from django.contrib import auth

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
    """'Аутентификация пользователя"""

    def post(self, request):

        login = request.POST['login']
        password = request.POST['password']

        user = auth.authenticate(username=login, password=password)

        if user is not None:
            auth.login(request, user)
            return Response(
                status=200, data={'message': 'Авторизация прошла успешно'})
        else:
            return Response(
                status=401, data={'message': 'Неверный логин или пароль'})


class LogoutView(APIView):
    """'Выход пользователя"""

    def post(self, request):

        auth.logout(request)

        return Response(
                status=200, data={'message': 'Выход прошел успешно'})
