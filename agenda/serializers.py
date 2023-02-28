from rest_framework import serializers
from agenda.models import Agendamento
from datetime import datetime
from django.utils import timezone

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id','data_horario','nome_cliente','email_cliente','telefone_cliente']
    # data_horario = serializers.DateTimeField()
    # nome_cliente = serializers.CharField(max_length=200)
    # email_cliente = serializers.EmailField()
    # telefone_cliente = serializers.CharField(max_length=20)

    def validate_data_horario(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Agendamento não pode ser feita no passado")
        return value
    
    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        email_cliente = attrs.get("email_cliente","")
        if email_cliente.endswith(".br") and telefone_cliente.startswith("+") and not telefone_cliente.startswith("+55"):
            raise serializers.ValidationError("Email do Brasil deve eesta associado a um numero do Brasil")
        return attrs
    