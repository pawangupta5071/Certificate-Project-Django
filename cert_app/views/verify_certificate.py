from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def verify_certificate(request):
    from cert_app.models import Certificate
    from rest_framework.response import Response
    from rest_framework import status

    try:
        # we have a JSON payload with certificate_id
        certificate_id = request.data.get('certificate_id')
        certificate = Certificate.objects.get(pk=certificate_id)

        # Verify the certificate based on your logic
        # Here, we're just checking if the user making the request is the teacher associated with the certificate
        if request.user.username == certificate.teacher.name:
            return Response({'message': 'Certificate verification successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Unauthorized to verify this certificate'}, status=status.HTTP_401_UNAUTHORIZED)

    except Certificate.DoesNotExist:
        return Response({'error': 'Certificate not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

