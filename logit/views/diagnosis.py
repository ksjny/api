import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from logit.models import Diagnosis

def diagnosis(request):
    if request.method == 'POST':
        return create_diagnosis(request)
    if request.method == 'GET':
        return get_diagnosis(request)

    return JsonResponse({'error': 'WRONG_METHOD'}, status=405)

def create_diagnosis(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'INVALID_JSON'}, status=400)

    try:
        name, severity = (data[k] for k in ('name', 'severity'))
    except KeyError:
        return JsonResponse({'error': 'MISSING_KEY'}, status=400)

    try:
        new = Diagnosis(
            name=name,
            severity=severity,
            user=request.user)
        new.save()
    except ValidationError:
        return JsonResponse({'error': 'INVALID_FIELD'}, status=400)

    return JsonResponse(new.to_dict(), status=201)

def get_diagnosis(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    diagnosiss = Diagnosis.objects.filter()
    diagnosis_dicts = [x.to_dict() for x in diagnosiss]
    return JsonResponse(diagnosis_dicts, safe=False)

def diagnosis_id(request, diagnosis_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    try:
        diagnosis = Diagnosis.objects.get(id=diagnosis_id)

    except Diagnosis.DoesNotExist:
        return JsonResponse({'error': 'INVALID_USER'}, status=404)

    if request.method == 'GET':
        return JsonResponse(diagnosis.to_dict())
    if request.method == 'DELETE':
        return delete_diagnosis(request, diagnosis)

def delete_diagnosis(request, diagnosis):
    diagnosis.delete()
    return HttpResponse('OK')
