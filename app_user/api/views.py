from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User

from app_user.api.serializers import RegistrationSerializer
from app_user import models


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration successful"
            data['account'] = account.username
            data['email'] = account.email

            # for user in User.objects.all():
            #   Token.objects.get_or_create(user=user)
            token = Token.objects.get(user=account)
            data['token'] = token.key

        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['POST', ])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
