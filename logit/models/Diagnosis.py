from django.db import models

class Diagnosis(models.Model):
    name = models.CharField(max_length=120)
    severity = models.CharField(max_length=120)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # utility method for printing
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'severity': self.severity
        }

    def __str__(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=2)
