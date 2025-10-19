from rest_framework import viewsets, status
from rest_framework.response import Response
from peaks.models import Pereval_added
from peaks.serializers import PerevalSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['get', 'post', 'patch']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            pereval = serializer.save()
            return Response({
                'status': 200,
                'message': 'Отправлено успешно',
                'id': pereval.id
            })
        else:
            return Response({
                "status": 400,  # Статус код лучше сменить на 400 Bad Request
                "message": "Некорректные данные",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
