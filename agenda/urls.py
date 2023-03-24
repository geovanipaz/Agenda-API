from django.urls import path
from agenda.views import  AgendamentoList, AgendamentoDetail

urlpatterns = [
    path('agendamento/', AgendamentoList.as_view()),
    path('agendamento/<int:pk>/', AgendamentoDetail.as_view())
]
