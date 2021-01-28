from rest_framework import serializers
from .models import Dostawca, Nadawca, Odbiorca, Paczka, Harmonogrampracy, Zamowienie


class DostawcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dostawca
        fields = ['nazwa_firmy', 'koszt_dostawy', 'sposob_platnosci', 'url']


class NadawcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nadawca
        fields = ['imie', 'nazwisko', 'adres_nadawcy', 'url']


class OdbiorcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Odbiorca
        fields = ['imie', 'nazwisko', 'adres_odbiorcy', 'url']


class PaczkaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paczka
        fields = ['waga', 'url']


class ZamowienieSerializer(serializers.HyperlinkedModelSerializer):
    nadawca = serializers.HyperlinkedRelatedField(many=False, read_only=False, queryset=Nadawca.objects.all(), view_name='nadawca-detail')
    odbiorca = serializers.HyperlinkedRelatedField(many=False, read_only=False, queryset=Odbiorca.objects.all(), view_name='odbiorca-detail')
    dostawca = serializers.HyperlinkedRelatedField(many=False, read_only=False, queryset=Dostawca.objects.all(), view_name='dostawca-detail')
    paczka = serializers.HyperlinkedRelatedField(many=False, read_only=False, queryset=Paczka.objects.all(),view_name='paczka-detail')
    class Meta:
        model = Zamowienie
        fields = ['podziekowanie', 'adres_zamowienia', 'data_zamowienia', 'url']




class HarmonogrampracySerializer(serializers.HyperlinkedModelSerializer):
    dostawca = serializers.HyperlinkedRelatedField(many=False, read_only=False, queryset=Dostawca.objects.all(),view_name='dostawca-detail')
    class Meta:
        model = Harmonogrampracy
        fields = ['godziny_pracy', 'url']



