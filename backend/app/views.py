from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import JsonResponse
from graphql_jwt.shortcuts import get_token
from django.views.decorators.csrf import csrf_exempt
import json

COOKIE_NAME = 'accessToken'
COOKIE_MAX_AGE = 60*60*24

@csrf_exempt
def login_view(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST allowed"}, status=405)
    
    try:
        body = json.loads(request.body)
        username = body.get("username")
        password = body.get("password")
    except (json.JSONDecodeError, KeyError):
        return JsonResponse({"error": "Invalid input"}, status=400)
    
    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    
    token = get_token(user)

    response = JsonResponse({"success": True})
    response.set_cookie(
        key=COOKIE_NAME,
        value=token,
        httponly=True,
        samesite='Strict',
        secure=True,
        max_age=COOKIE_MAX_AGE
    )
    return response

@csrf_exempt
def logout_view(request):
    response = JsonResponse({"success": True})
    response.delete_cookie(COOKIE_NAME)
    return response

@api_view(['GET'])
def hello_world(request):
    print(">>> hello_world view was hit")
    return Response({'message': 'Hello from Django!'})
