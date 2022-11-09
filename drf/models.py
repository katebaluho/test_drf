from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name="profile")
    inn = models.CharField(max_length=15, null=True, verbose_name='ИНН')
    account = models.FloatField(null=True, verbose_name='Счёт')

    class Meta:
        unique_together = ['user', 'inn']

    def __str__(self):
        return '{id} {inn}'.format(id=str(self.id), inn=self.inn)

