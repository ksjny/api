import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from logit.models import Medication

def medication(request):
    if request.method == 'POST':
        return create_medication(request)
    if request.method == 'GET':
        return get_medication(request)

    return JsonResponse({'error': 'WRONG_METHOD'}, status=405)

def create_medication(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'INVALID_JSON'}, status=400)

    try:
        name, time_period = (data[k] for k in ('name', 'time_period'))
    except KeyError:
        return JsonResponse({'error': 'MISSING_KEY'}, status=400)

    try:
        new = Medication(
            name=name,
            time_period=time_period,
            user=request.user)
        new.save()
    except ValidationError:
        return JsonResponse({'error': 'INVALID_FIELD'}, status=400)

    return JsonResponse(new.to_dict(), status=201)

def get_medication(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    medications = Medication.objects.filter()
    medication_dicts = [x.to_dict() for x in medications]
    return JsonResponse(medication_dicts, safe=False)

def medication_id(request, medication_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'NOT_AUTHENTICATED'}, status=403)

    try:
        medication = Medication.objects.get(id=medication_id)

    except Medication.DoesNotExist:
        return JsonResponse({'error': 'INVALID_USER'}, status=404)

    if request.method == 'GET':
        return JsonResponse(medication.to_dict())
    if request.method == 'DELETE':
        return delete_medication(request, medication)

def delete_medication(request, medication):
    medication.delete()
    return HttpResponse('OK')
