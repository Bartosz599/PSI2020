from rest_framework import serializers
import datetime


class DostawcaSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.nazwa_firmy = validated_data.get('nazwa_firmy',instance.nazwa_firmy)
        instance.koszt_dostawy = validated_data.get('koszt_dostawy', instance.koszt_dostawy)
        instance.sposob_platnosci = validated_data.get('sposob_platnosci', instance.sposob_platnosci)
        instance.save()
        return instance

    def create(self, validated_data):

    nazwa_firmy = serializers.CharField(max_length=45)
    koszt_dostawy = serializers.IntegerField
    sposob_platnosci = serializers.CharField(max_length=45)




class KlientSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miejscowosc = validated_data.get('miejscowosc', instance.miejscowosc)
        instance.id_dostawca = validated_data.get('id_dostawca', instance.id_dostawca)
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    imie = serializers.CharField(max_length=45)
    nazwisko = serializers.CharField(max_length=45)
    miejscowosc = serializers.CharField(max_length=45)
    id_dostawca = serializers.ForeignKey(DostawcaSerializer, on_delete=serializers.CASCADE)




class PaczkaSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.waga = validated_data.get('waga', instance.waga)
        instance.cena = validated_data.get('cena', instance.cena)
        instance.id_dostawca = validated_data.get('id_dostawca', instance.id_dostawca)
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    waga = serializers.IntegerField
    cena = serializers.IntegerField
    id_dostawca = serializers.ForeignKey(DostawcaSerializer, on_delete=serializers.CASCADE)




class ZamowienieSerializer(serializers.Serializer):

    def data_zamowienia(self, data_zamowienia):
        if data_zamowienia <= datetime.datetime.now():
            return data_zamowienia
        return data_zamowienia

    def update(self, instance, validated_data):
        instance.podziekowanie = validated_data.get('podziekowanie', instance.podziekowanie)
        instance.adres_zamowienia = validated_data.get('adres_zamowienia', instance.adres_zamowienia)
        instance.data_zamowienia = validated_data.get('data_zamowienia', instance.data_zamowienia)
        instance.id_dostawca = validated_data.get('id_dostawca', instance.id_dostawca)
        instance.id_klient = validated_data.get('id_klient', instance.id_klient)
        instance.id_paczka = validated_data.get('id_paczka', instance.id_paczka)
        instance.save()
        return instance

    def create(self, validated_data):
        pass


    podziekowanie = serializers.TextField()
    adres_zamowienia = serializers.CharField(max_length=45)
    data_zamowienia = serializers.DateField()
    id_dostawca = serializers.ForeignKey(DostawcaSerializer,on_delete=serializers.CASCADE)
    id_klient = serializers.ForeignKey(KlientSerializer, on_delete=serializers.CASCADE)
    id_paczka = serializers.ForeignKey(PaczkaSerializer, on_delete=serializers.CASCADE)





