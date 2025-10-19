from django.forms import model_to_dict
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



    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        user_dict = model_to_dict(pereval.user)
        user_dict.pop('id')
        serializer = self.get_serializer(pereval, data=request.data, partial=True)
        update_pereval = check_update_pereval(request, pereval, user_dict)
        if update_pereval:
            return update_pereval
        serializer.is_valid(raise_exceptions=True)
        serializer.save()
        return update_response()

