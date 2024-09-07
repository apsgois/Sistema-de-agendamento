from django.urls import path
from core.views.patient_view import create_patient_view, get_patients_view, update_patient_view, delete_patient_view
from core.views.appointment_view import create_appointment_view, get_appointments_view,get_appointments_by_id_view, update_appointment_view, delete_appointment_view
urlpatterns = [
   
    path('patients/', get_patients_view, name='get-patient'),
    path('patients/create/', create_patient_view, name='create-patient'),
    path('patients/<str:cpf>/', update_patient_view, name='update-patient'),
    path('patients/delete/<str:cpf>/', delete_patient_view, name='delete-patient'),
    
    path('appointments/', get_appointments_view, name='get-appointments'),
    path('appointments/create/', create_appointment_view, name='create-appointment'),
    path('appointments/<int:patient>/', get_appointments_by_id_view, name='get-appointment-by-id'),
    path('appointments/<int:id>/update/', update_appointment_view, name='update-appointment'),
    path('appointments/<int:id>/delete/', delete_appointment_view, name='delete-appointment'),
]