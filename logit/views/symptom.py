import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from logit.models import Symptom, User

def symptom(request):
    if request.method == 'POST':
        return create_symptom(request)
    if request.method == 'GET':
        return get_symptom(request)

    return JsonResponse({'error': 'WRONG_METHOD'}, status=405)

def create_symptom(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'INVALID_JSON'}, status=400)

    try:
        location, severity, pain_type = (data[k] for k in ('location', 'severity', 'pain_type'))
    except KeyError:
        return JsonResponse({'error': 'MISSING_KEY'}, status=400)

    # user = User.objects.filter()[0]

    try:
        new = Symptom(
            location=location,
            severity=severity,
            pain_type=pain_type,
            user=request.user)
        new.save()
    except ValidationError:
        return JsonResponse({'error': 'INVALID_FIELD'}, status=400)

    return JsonResponse(new.to_dict(), status=201)

def get_symptom(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    symptoms = Symptom.objects.filter()
    symptom_dicts = [x.to_dict() for x in symptoms]
    return JsonResponse(symptom_dicts, safe=False)

def symptom_id(request, symptom_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    try:
        symptom = Symptom.objects.get(id=symptom_id)

    except Symptom.DoesNotExist:
        return JsonResponse({'error': 'INVALID_USER'}, status=404)

    if request.method == 'GET':
        return JsonResponse(symptom.to_dict())
    if request.method == 'DELETE':
        return delete_symptom(request, symptom)

def delete_symptom(request, symptom):
    symptom.delete()
    return HttpResponse('OK')
