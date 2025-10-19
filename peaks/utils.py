from rest_framework import status
from rest_framework.response import Response

def check_user_dict(user_dict, request_dict_user):
    common_keys = user_dict.keys()&request_dict_user.keys()
    new_user_dict = {key: user_dict[key] for key in common_keys}
    return new_user_dict != request_dict_user


def update_response():
    return Response({
                'status': 200,
                'message': 'Отправлено успешно',
                'id': None})
def check_update_pereval(request, pereval, user_dict):
    if pereval.status != "new":
        return Response(
            {'state': 0, 'message': 'Изменять запись можно только в статусе "new"'},
            status=status.HTTP_400_BAD_REQUEST
        )
    print(request.data.get("user"))
    print(check_user_dict(user_dict, request.data.get("user")))
    if check_user_dict(user_dict, request.data.get("user")):
        return Response(
            {'state': 0, 'message': 'нельзя менять данные пользователя'},
            status=status.HTTP_400_BAD_REQUEST
        )
    return False