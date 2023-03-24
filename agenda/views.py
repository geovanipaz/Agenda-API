from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from agenda.models import Agendamento
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from agenda.serializers import AgendamentoSerializer
# Create your views here.

class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView):#/api/agendamento/<pk>/
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request,*args, **kwargs)
    # def patch(self,request,*args, **kwargs):
    #     return self.partial_update(request,*args, **kwargs)
    # def put(self,request,*args, **kwargs):
    #     return self.update(request,*args, **kwargs)
    # def delete(self, request,*args, **kwargs):
    #     return self.destroy(request,*args, **kwargs)

# @api_view(http_method_names=["GET","PATCH","DELETE"])
# def agendamento_detail(request, id):
#     obj = get_object_or_404(Agendamento, id=id)
#     if request.method == "GET":
#         serializer = AgendamentoSerializer(obj)
#         return JsonResponse(serializer.data)
#     if request.method == "PATCH":
#         serializer = AgendamentoSerializer(obj,data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)
#     if request.method == "DELETE":
#         obj.delete()
#         return Response(status=204)

class AgendamentoList(generics.ListCreateAPIView): #/api/agendamento/?username=geovani
    #queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        queryset = Agendamento.objects.filter(prestador__username=username)
        return queryset

    # def get(self, request,*args, **kwargs):
    #     return self.list(request,*args, **kwargs)
        
    # def post(self, request,*args, **kwargs):
    #     return self.create(request, *args, **kwargs)

# @api_view(http_method_names=["GET","POST"])
# def agendamento_list(request):
#     if request.method == "GET":
#         qs = Agendamento.objects.all()
#         serializer = AgendamentoSerializer(qs, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     if request.method == "POST":
#         data = request.data
#         serializer = AgendamentoSerializer(data=data)
#         if serializer.is_valid():
#             validated_data = serializer.validated_data
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=404)



