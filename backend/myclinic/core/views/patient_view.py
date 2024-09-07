from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.services.patient_service import create_patient, get_patients, get_patient_by_cpf, update_patient, delete_patient, UpdatePatientError
from core.serializers import PatientSerializer

@api_view(['POST'])
def create_patient_view(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        create_patient(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_patients_view(request):
    return Response(PatientSerializer(get_patients(), many=True).data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_patient_view(request, cpf):
    try:
        updated_patient = update_patient(cpf, request.data)
        serializer = PatientSerializer(updated_patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    except UpdatePatientError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_patient_view(request, cpf):
    try:
        patient = get_patient_by_cpf(cpf=cpf)
    except:
        return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        delete_patient(cpf)
        return Response({'message': 'Paciente deletado'},status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)


    