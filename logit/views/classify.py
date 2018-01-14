import numpy as np
from .constants import *

from logit.models import User, Symptom, Diagnosis

SYMPTOM_LOCATION_COUNT = 15
SYMPTOM_INTENSITY_COUNT = 5
SYMPTOM_SENSATION_COUNT = 4

def classify(request, user_id):
    user_to_classify = User.objects.filter(id=user_id)

    users = User.objects.filter()
    instance_array = [SYMPTOM_SENSATION_COUNT*SYMPTOM_INTENSITY_COUNT*SYMPTOM_LOCATION_COUNT][len(users)]

    user_diagnosis_count = 0

    for user in users:
        diagnosiss = Diagnosis.objects.filter(user=user)
        for diagnosis in diagnosiss:
            symptoms = Symptom.objects.filter(user=user)
            for symptom in symptoms:
                print(symptom)
                instance_array[user_diagnosis_count][SYMPTOM_LOCATION[symptom*3]] = 1
