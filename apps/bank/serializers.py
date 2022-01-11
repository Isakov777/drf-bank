from django.db import models
from django.http import request
from rest_framework import fields, serializers
from apps.bank.models import Action,  Transfer,Schet, Transaction
from apps.user.models import User



class SchetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schet
        fields = ('id', 'user', 'scheta',  'balance')
        read_only_fields = ('balance', )

class ActionSerializer(serializers.ModelSerializer):

   

    class Meta:
        model = Action
        fields = ('id', 'amount', 'schet')
        read_only_fields = ('id',)

    def create(self, validated_data):
        if validated_data['schet'].balance + validated_data['amount'] > 0:
            validated_data['schet'].balance += validated_data['amount']
            validated_data['schet'].save()
        else:
            raise serializers.ValidationError(
                ('Not sufficient money')
            )
        return super(ActionSerializer, self).create(validated_data)

    


class TransferSerializer(serializers.ModelSerializer):

    
    to_schet = serializers.CharField()
    
    def validate(self, data):
        try:
            data['to_schet'] = Schet.objects.get(scheta = data['to_schet'])
        except Exception as e:
            print(e)
            raise serializers.ValidationError(('No such schet'))
        return data

    class Meta:
        model = Transfer
        fields = ('id', 'from_schet', 'to_schet', 'amount')
        read_only_fields = ('id',)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'schet', 'title')