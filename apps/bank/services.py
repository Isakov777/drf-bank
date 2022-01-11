from apps.bank.models import  Schet, Transfer
from django.db import transaction
from django.core.exceptions import ValidationError

def make_transfer(from_schet, to_schet, amount):


    if from_schet.balance < amount:
        raise(ValidationError('Not enough money'))
    if from_schet == to_schet:
        raise(ValidationError('Chose another account'))
    
    with transaction.atomic():
        from_balance = from_schet.balance - amount
        from_schet.balance = from_balance
        from_schet.save()

        to_balance = to_schet.balance + amount
        to_schet.balance = to_balance
        to_schet.save()

        transfer = Transfer.objects.create(
            from_schet = from_schet,
            to_schet = to_schet,
            amount = amount
        )

    return transfer


# def filter_user_account(user, account_id):
#     try:
#         account = Account.objects.filter(
#             user = user).get(pk = account_id)
#     except (Account.DoesNotExist):
#         raise ValidationError('Account does not exist')
#     return account

# def check_account_exists(account_id):
#     try:
#         account = Account.objects.get(pk = account_id)
#     except Exception as e:
#         print(e)
#         raise ValidationError('No such account')
#     return account

# def make_transfer():
#     schets = Schet.objects.all()
#     for schet in schets:
#         with transaction.atomic():
#             pr = 0.08 / 12
#             balance = float(schet.balance)
#             history = balance * pr
#             balance += history
#             schet.balance = balance
            

#             schet.save()