#from django.test import TestCase
from rest_framework.test import APITestCase
from agenda.models import Agendamento
from datetime import datetime, timezone
import json


class TesteListagemAgendamento(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamento/")
        data = json.loads(response.content)
        self.assertEqual(data, [])

    def test_de_agendamentos_criados(self):
        Agendamento.objects.create(
            data_horario=datetime(2023,4,14, tzinfo=timezone.utc),
            nome_cliente="alice",
            email_cliente="alice@email.com",
            telefone_cliente="99998888",
        )
        agendamento_serializado = {
            "id":1,
            "data_horario":"2023-04-14T00:00:00Z",
            "nome_cliente":"alice",
            "email_cliente":"alice@email.com",
            "telefone_cliente":"99998888",
        }
        response = self.client.get("/api/agendamento/")
        data = json.loads(response.content)
        self.assertDictEqual(data[0], agendamento_serializado)

class TestCriacaoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        agendamento_request_data = {
            "data_horario":"2023-04-14T00:00:00Z",
            "nome_cliente":"alice",
            "email_cliente":"alice@email.com",
            "telefone_cliente":"99998888",
        }
        response = self.client.post("/api/agendamento/", agendamento_request_data, format="json")
        agendamento_criado = Agendamento.objects.get()

        self.assertEqual(agendamento_criado.data_horario, datetime(2023,4,14, tzinfo=timezone.utc))
        self.assertEqual(response.status_code, 201)
    
    def test_quando_request_e_invalido_retorna_400(self):
        agendamento_request_data = {
            "data_horario":"2023-04-14T00:00:00Z",
            "nome_cliente":"alice",
            "email_cliente":"alice@email.com",
            "telefone_cliente":"99998888",
        }
        response = self.client.post("/api/agendamento/", agendamento_request_data, format="json")
        response_get = self.client.get("/api/agendamento/")
        agendamento_criado = Agendamento.objects.get()
        self.assertEqual(agendamento_criado.nome_cliente, "alice")