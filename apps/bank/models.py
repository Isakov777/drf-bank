
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import DecimalValidator, MaxLengthValidator, MinLengthValidator

from django.db.models.deletion import CASCADE, PROTECT
from django.db import transaction
# from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework import validators

User = get_user_model()



class Schet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='customer')
    scheta = models.DecimalField(max_digits=8, decimal_places=0, validators = [
        DecimalValidator(
            max_digits=5,
            decimal_places=0,
        )
    ])
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0) 


    def __str__(self) -> str:
        return str(self.scheta)

    def full_clean(self, exclude, validate_unique):
        return super().full_clean(exclude=exclude, validate_unique=validate_unique)







class Action(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    schet = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='action_schet')


    def __str__(self) -> str:
        return f'User {self.schet.id} + {self.amount}'





class Transfer(models.Model):
    from_schet = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='from_schet')
    to_schet = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='transfer_to_schet')
    amount = models.DecimalField(max_digits=12, decimal_places=2)



class Transaction(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    schet = models.ForeignKey(Schet, on_delete=models.CASCADE, related_name='transaction_schet')
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Schet {self.schet.id} sent {str(self.amount)} to {self.title}'
    
    @classmethod
    def make_transaction(cls, amount, schet, title):
        if schet.balance < amount:
            raise(ValueError('Not sufficient money'))

        with transaction.atomic():
            schet.balance -= amount
            schet.save()
            tran = cls.objects.create(amount = amount, schet = schet, title = title)

        return schet, tran  