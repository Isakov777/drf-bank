from django.contrib import admin

from apps.bank.models import   Action, Schet, Transfer, Transaction



admin.site.register(Action)
admin.site.register(Schet)

admin.site.register(Transfer)
admin.site.register(Transaction)
