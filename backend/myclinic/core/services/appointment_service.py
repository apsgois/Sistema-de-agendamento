from core.models.appointment import Appointment
from django.http import Http404

def create_appointment(data):
    return Appointment.objects.create(**data)

def update_appointment(id, data):
    try:
        
        appointment = Appointment.objects.get(id=id)
        for key, value in data.items():
            setattr(appointment, key, value)
        appointment.save()
        return appointment
    except Appointment.DoesNotExist:
        raise Http404("Appointment does not exist.")

def get_appointment():
    return Appointment.objects.all()

def delete_appointment(id):
    try:
        return Appointment.objects.get(id=id).delete()
    except:
        raise Http404("Appointment does not exist")

def get_appointments_by_patient(patient):
    appointments = Appointment.objects.filter(patient=patient)
    if appointments.exists():
        return appointments
    else:
        raise Http404("No appointments found for this patient.")