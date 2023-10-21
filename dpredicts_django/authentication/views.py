from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import random
import string
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from django.shortcuts import get_object_or_404

@csrf_exempt
def check_email(request):
    if request.method == 'POST':
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            reset_token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            user.reset_token = reset_token
            user.save()
            return JsonResponse({'exists': True, 'reset_token': reset_token})
        except User.DoesNotExist:
            return JsonResponse({'exists': False})
    return JsonResponse({'exists': False, 'message': 'Invalid request.'})

@api_view(['GET'])
def user_profile(request):
    # Get the user profile for the currently authenticated user
    user = get_object_or_404(User, pk=request.user.pk)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)