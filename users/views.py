
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            # Логин успешен, возвращаем данные о пользователе
            return Response(
                {
                    "username": user.username,
                    "email": user.email,
                }
            )
        else:
            return Response({"error": "Invalid credentials"}, status=400)
