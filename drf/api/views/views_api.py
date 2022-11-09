from django.db.models import Model
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from drf.api.serializers.serializers import TransferSerializer
from drf.api.views.calculate_amount import amount_every_recipients


class TransferViewSet(viewsets.ViewSet):
    serializer_class = TransferSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.data)

            user_sender = User.objects.get(id=serializer.data['user_sender'])

            if user_sender.profile.account < serializer.data['amount']:
                return Response('На счёте недостаточно средств',
                                status=status.HTTP_200_OK)

            recipients = User.objects.filter(profile__inn__in=serializer.data['inn_recipients'])

            if not recipients:
                return Response('Получатели не найдены',
                                status=status.HTTP_200_OK)
            if user_sender in recipients:
                return Response('Невозможно отправить сумму на ИНН отправителя, проверьте список ИНН',
                                status=status.HTTP_200_OK)

            transfer_amount = amount_every_recipients(serializer.data['amount'], recipients.count())
            for recipient in recipients:   #TODO: здесь бы я еще продумала/поискала информацию о проверке действий со счетом.
                recipient.profile.account += transfer_amount
                user_sender.profile.account -= transfer_amount
                user_sender.profile.save()
                recipient.profile.save()

            return Response('Перевод совершен',
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

