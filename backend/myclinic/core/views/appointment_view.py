from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.serializers import AppointmentSerializer
from core.services.appointment_service import create_appointment, update_appointment, get_appointment, delete_appointment, get_appointments_by_patient
from django.http import Http404

@api_view(['POST'])
def create_appointment_view(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        create_appointment(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_appointments_view(request):
    return Response(AppointmentSerializer(get_appointment(), many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_appointments_by_id_view(request, patient):
     
    appointments = get_appointments_by_patient(patient)
    serialized_appointments = AppointmentSerializer(appointments, many=True)
    return Response( serialized_appointments.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_appointment_view(request, id):
    try:
        print("Id", id)
        appointment = update_appointment(id, request.data)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        raise Http404("Appointment does not exist.")
    

@api_view(['DELETE'])
def delete_appointment_view(request, id):
    try:
        delete_appointment(id=id)
        return Response({'message': 'Appointment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except:
        return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    
