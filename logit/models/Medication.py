from django.db import models

from . import User

class Medication(models.Model):
    name = models.CharField(max_length=120)
    time_period = models.DurationField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'timePeriod': self.time_period,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat(),
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)
