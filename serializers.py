from rest_framework import serializers
from nadawaniepaczek.nadawaniepaczek.models import Dostawca
from nadawaniepaczek.nadawaniepaczek.models import Klient
from nadawaniepaczek.nadawaniepaczek.models import Paczka
from nadawaniepaczek.nadawaniepaczek.models import Zamowienie


class KlasaDostawca(serializers.ModelSerializer):
    class Meta:
        model = Dostawca
        fields = '__all__'

class KlasaKlient(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'


class KlasaPaczka(serializers.ModelSerializer):
    class Meta:
        model = Paczka
        fields = '__all__'


class KlasaZamowienie(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields = '__all__'
