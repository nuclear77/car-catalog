from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def home(request):
    return render(request, "home.html")

#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def protected_view(request):
#     user = request.user
#     return Response({'message': f'Hello, {user.username}! This is a protected view.'})