from django.shortcuts import render
from django.http import HttpResponse
from django_filters import NumberFilter, FilterSet
from .serializers import DostawcaSerializer, NadawcaSerializer, OdbiorcaSerializer, \
    ZamowienieSerializer, HarmonogrampracySerializer, PaczkaSerializer
from .models import Dostawca, Nadawca, Odbiorca, Harmonogrampracy, Zamowienie, Paczka
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("<h1>Strona główna Nadawania Paczek</h1>")


class DostawcaList(generics.ListCreateAPIView):
    queryset = Dostawca.objects.all()
    serializer_class = DostawcaSerializer
    name = 'dostawca-list'
    filter_fields = ['nazwa_firmy', 'koszt_dostawy', 'sposob_platnosci']
    search_fields = ['nazwa_firmy']
    ordering_fields = ['koszt_dostawy']
    permission_classes = [permissions.IsAuthenticated]


class DostawcaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dostawca.objects.all()
    serializer_class = DostawcaSerializer
    name = 'dostawca-detail'
    permission_classes = [permissions.IsAuthenticated]


class NadawcaList(generics.ListCreateAPIView):
    queryset = Nadawca.objects.all()
    serializer_class = NadawcaSerializer
    name = 'nadawca-list'
    filter_fields = ['imie', 'nazwisko', 'adres_nadawcy']
    ordering_fields = ['imie', 'nazwisko']


class NadawcaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nadawca.objects.all()
    serializer_class = NadawcaSerializer
    name = 'nadawca-detail'


class OdbiorcaList(generics.ListCreateAPIView):
    queryset = Odbiorca.objects.all()
    serializer_class = OdbiorcaSerializer
    name = 'odbiorca-list'
    filter_fields = ['imie', 'nazwisko', 'adres_odbiorcy']
    ordering_fields = ['imie', 'nazwisko']
    permission_classes = [permissions.IsAuthenticated]


class OdbiorcaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odbiorca.objects.all()
    serializer_class = OdbiorcaSerializer
    name = 'odbiorca-detail'
    permission_classes = [permissions.IsAuthenticated]


class PaczkaList(generics.ListCreateAPIView):
    queryset = Paczka.objects.all()
    serializer_class = PaczkaSerializer
    name = 'paczka-list'
    filter_fields = ['waga']
    ordering_fields = ['waga']
    permission_classes = [permissions.IsAuthenticated]


class PaczkaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paczka.objects.all()
    serializer_class = PaczkaSerializer
    name = 'paczka-detail'
    permission_classes = [permissions.IsAuthenticated]


class ZamowienieList(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienie-list'
    filter_fields = ['podziekowanie', 'adres_zamowienia', 'data_zamowienia']
    ordering_fields = ['data_zamowienia']
    permission_classes = [permissions.IsAuthenticated]


class ZamowienieDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienie-detail'
    permission_classes = [permissions.IsAuthenticated]

class HarmonogrampracyFilter(FilterSet):
    godziny_min = NumberFilter(field_name='godziny_pracy', lookup_expr='gte')
    godziny_max = NumberFilter(field_name='godziny_pracy', lookup_expr='lte')

    class Meta:
        model = Harmonogrampracy
        fields = ['godziny_min', 'godziny_max']

class HarmonogrampracyList(generics.ListCreateAPIView):
    queryset = Harmonogrampracy.objects.all()
    serializer_class = HarmonogrampracySerializer
    name = 'harmonogrampracy-list'
    filter_fields = ['godziny_pracy']
    ordering_fields = ['godziny_pracy']
    permission_classes = [permissions.IsAuthenticated]


class HarmonogrampracyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Harmonogrampracy.objects.all()
    serializer_class = HarmonogrampracySerializer
    name = 'harmonogrampracy-detail'
    permission_classes = [permissions.IsAuthenticated]



class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, req, *args, **kwargs):
        return Response({'lista-dostawcow': reverse(DostawcaList.name, request=req),
                         'lista-nadawcow': reverse(NadawcaList.name, request=req),
                         'lista-odbiorcow': reverse(OdbiorcaList.name, request=req),
                         'lista-paczek': reverse(PaczkaList.name, request=req),
                         'lista-zamowien': reverse(ZamowienieList.name, request=req),
                         'lista-harmonogramowpracy': reverse(HarmonogrampracyList.name, request=req),

                         })

