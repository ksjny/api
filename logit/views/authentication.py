import json

from django.shortcuts import HttpResponse

from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout

from logit.models import User

def authenticateuser(request):
    if request.method == 'POST':
        return login_user(request)
    elif request.method == 'GET':
        return get_current_user(request)
    else:
        return JsonResponse({'error': 'WRONG_METHOD'}, status=405)

def login_user(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'INVALID_JSON'}, status=400)

    try:
        email, password = (data[k] for k in ('email', 'password'))
    except KeyError:
        return JsonResponse({'error': 'MISSING_KEY'}, status=400)

    try:
        User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'error': 'USER_NOT_FOUND'}, status=404)

    user = authenticate(request, email=email, password=password)

    if not user:
        return JsonResponse({'error': 'INVALID_PASSWORD'}, status=400)

    login(request, user)

    return JsonResponse(user.to_dict())

def get_current_user(request):
    if request.user.is_authenticated:
        return JsonResponse(request.user.to_dict())
    else:
        return JsonResponse({'error': 'USER_NOT_FOUND'}, status=404)

def signout(request):
    logout(request)
    return HttpResponse('OK')
