from django.db import models

class Patient(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255)
    address_number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    whatsapp = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.name