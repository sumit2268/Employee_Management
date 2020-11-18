from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from ..serializers.loginSerializer import LoginSerializer
from rest_framework import status
from django.contrib.auth import login as django_login
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import logout
class LoginApiView(GenericAPIView):
    authentication_classes=()
    permission_classes=()
    serializer_class=LoginSerializer
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            django_login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key,"userId":user.id}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Logout(APIView):
    def get(self, request, format=None):
        logout(request)
        # simply delete the token to force a login
        return Response(status=status.HTTP_200_OK)