from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from logit.models import User, Symptom, Diagnosis, Medication

class Command(BaseCommand):
    help = "Populates a basic set of test data"

    def handle(self, *args, **options):
        userData = {
            'email': 'test@test.com',
            'password': 'test',
            'first_name': 'tester',
            'last_name': 'liefbase',
        }
        try:
            user = User.objects.get(email=userData['email'])
            created = False
        except User.DoesNotExist:
            user = User.objects.create_user(**userData)
            created = True
        print("Test User{} Created".format('' if created else ' Not'))
        print(user)
        print()

        Symptom.objects.bulk_create([
            Symptom(location='Right Knee', severity=4, pain_type='Moaning', user=user),
            Symptom(location='Right Quad', severity=4, pain_type='Stabbing', user=user),
            Symptom(location='Right Calf', severity=2, pain_type='Moaning', user=user),
            Symptom(location='Right Hip', severity=1, pain_type='Stabbing', user=user),
            Symptom(location='Right Ankle', severity=4, pain_type='Stabbing', user=user),
            Symptom(location='Right Calf', severity=3, pain_type='Moaning', user=user),
            Symptom(location='Right Knee', severity=2, pain_type='Grinding', user=user),
            Symptom(location='Lower Back', severity=1, pain_type='Moaning', user=user)
        ])

        Diagnosis.objects.bulk_create([
            Diagnosis(name='Torn ACL (Right)', severity='Severe', user=user),
            Diagnosis(name='Strained MCL (Right)', severity='Moderate', user=user)
        ])

        Medication.objects.bulk_create([
            Medication(name='Tylenol 3', time_period='86400.00', user=user),
            Medication(name='Icing', time_period='86400.00', user=user)
        ])
