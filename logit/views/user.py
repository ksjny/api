import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse

from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from logit.models import User, UserManager

def user(request):
    if request.method == 'POST':
        return create_user(request)
    if request.method == 'GET':
        return get_user(request)

    return JsonResponse({'error': 'WRONG_METHOD'}, status=405)

def create_user(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'INVALID_JSON'}, status=400)

    try:
        first, last, email, password, cpassword, org_id = (data[k] for k in ('first_name', 'last_name', 'email', 'password', 'confirm_password'))
    except KeyError:
        return JsonResponse({'error': 'MISSING_KEY'}, status=400)

    if password != cpassword:
        return JsonResponse({'error': 'PASSWORDS_MUST_MATCH'}, status=400)

    try:
        validate_password(password)
    except ValidationError as e:
        return JsonResponse({'error': 'INVALID_PASSWORD', 'message': str(e)}, status=400)

    try:
        validate_email(email)
    except ValidationError as e:
        return JsonResponse({'error': 'INVALID_EMAIL', 'message': str(e)}, status=400)

    try:
        new = UserManager().create_user(first_name=first, last_name=last, email=email, password=password)
    except IntegrityError as e:
        return JsonResponse({'error': 'REGISTRATION_ERROR', 'message': str(e)}, status=400)

    return JsonResponse(new.to_dict(), status=201)

def get_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    if not request.user.permission == User.ADMIN:
        return JsonResponse({'error': 'NOT_ADMIN'}, status=403)

    users = User.objects.filter()
    user_dicts = [x.to_dict() for x in users]
    return JsonResponse(user_dicts, safe=False)

def user_id(request, user_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    try:
        user = User.objects.get(id=user_id)

        if not request.user.permission == User.ADMIN and not user == request.user:
            return JsonResponse({'error': 'NO_PERMISSION'}, status=401)

    except User.DoesNotExist:
        return JsonResponse({'error': 'INVALID_USER'}, status=404)

    if request.method == 'GET':
        return JsonResponse(user.to_dict())
    if request.method == 'DELETE':
        return delete_user(request, user)

def delete_user(request, user):
    user.delete()
    return HttpResponse('OK')
