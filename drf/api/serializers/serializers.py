from django.contrib.auth.models import User
from rest_framework import serializers


class TransferSerializer(serializers.Serializer):

    user_sender = serializers.ChoiceField(choices=User.objects.all().values_list('id', flat=True))
    inn_recipients = serializers.ListField()
    amount = serializers.FloatField()

    def parse_inn_recipients(self, value):
        return value[0].split(',')

    def validate_inn_recipients(self, inn_recipients):
        recipients = self.parse_inn_recipients(inn_recipients)
        for inn_value in recipients:
            if not inn_value.isdigit():
                raise serializers.ValidationError("Введено не числовое значение,проверьте список ИНН")
        return recipients
