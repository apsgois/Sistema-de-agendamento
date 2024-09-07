from core.models.patient import Patient


class UpdatePatientError(Exception):
    pass

def get_patients():
    return Patient.objects.all()

def get_patient_by_cpf(cpf):
    return Patient.objects.get(cpf=cpf)

def create_patient(data):
    return Patient.objects.create(**data)



def update_patient(cpf, data):
    try:
        patient = Patient.objects.get(cpf=cpf)
    except Patient.DoesNotExist:
        raise ValueError("Patient not found")
    
    if 'cpf' in data:
       raise UpdatePatientError("Cannot update the CPF field.")
    
    for key, value in data.items():
        setattr(patient, key, value)
    
    patient.save()
    return patient

def delete_patient(cpf):
    Patient.objects.get(cpf=cpf).delete()
    return None

def get_patient_by_cpe(cpe):
    return Patient.objects.get(cpe=cpe)