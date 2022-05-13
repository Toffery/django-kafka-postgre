from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .producer import send
from api_listener.settings import jwt_token


# Create your views here.
class MessageAPIView(APIView):
    """
    {
        "user_id": int,

        "message": text
    }
    """

    def post(self, request):
        # Save message to DB Message
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        mes = Message.objects.get(pk=serializer.data['id'])
        data = {
            'message_id': mes.pk,
            'success': None
        }
        # Save message_id and success to DB MessageConfirm
        serializer = MessageConfirmSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Send message to Kafka
        send(mes.pk, mes.message)

        return Response({'post': serializer.data})


class TextAPIUpdate(APIView):
    """
    {
        "message_id": int,

        "status": bool
    }
    """

    def post(self, request):
        if 'authorization' not in request.headers:
            return Response({'ERROR': 'No authorization token'})
        if request.headers['authorization'] != jwt_token:
            return Response({'ERROR': 'Token is incorrect'})
        # Update success on DB MessageConfirm
        mes_success = MessageConfirm.objects.get(message_id=request.data['message_id'])
        mes_success.success = request.data['success']
        mes_success.save()
        # Update status on DB Message
        mes_update = Message.objects.get(pk=request.data['message_id'])
        if mes_success.success:
            mes_update.status = 'correct'
            mes_update.save()
        else:
            mes_update.status = 'blocked'
            mes_update.save()
        return Response({'post': "success"})
