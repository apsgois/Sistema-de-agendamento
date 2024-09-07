from django.db import models

class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient.name} - {self.date} - {self.time}'
