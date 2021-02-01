from django.db import models

class Dostawca(models.Model):
    nazwa_firmy = models.CharField(max_length=45)
    koszt_dostawy = models.IntegerField(max_length=45)
    sposob_platnosci = models.CharField(max_length=45)

    def __str__(self):
        return self.nazwa_firmy


class Nadawca(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    adres_nadawcy = models.CharField(max_length=90)

    def __str__(self):
        return self.imie+' '+self.nazwisko


class Odbiorca(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    adres_odbiorcy = models.CharField(max_length=90)

    def __str__(self):
        return self.imie+' '+self.nazwisko



class Paczka(models.Model):
    waga = models.IntegerField(max_length=45)
    

    def __str__(self):
        return self.waga



class Harmonogrampracy(models.Model):
    godziny_pracy = models.CharField(max_length=5)
    id_dostawca = models.ForeignKey(Dostawca, related_name='harmonogrampracy', on_delete=models.CASCADE)

    def __str__(self):
        return self.godziny_pracy



class Zamowienie(models.Model):
    podziekowanie = models.TextField()
    adres_zamowienia = models.CharField(max_length=90)
    data_zamowienia = models.DateTimeField(auto_now_add=True, blank=True)
    id_dostawca = models.ForeignKey(Dostawca, related_name='zamowienie', on_delete=models.CASCADE)
    id_nadawca = models.ForeignKey(Nadawca, related_name='zamowienie', on_delete=models.CASCADE)
    id_paczka = models.ForeignKey(Paczka, related_name='zamowienie', on_delete=models.CASCADE)
    id_odbiorca = models.ForeignKey(Odbiorca, related_name='zamowienie', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.adres_zamowienia)








