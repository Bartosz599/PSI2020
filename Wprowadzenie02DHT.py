##
## 1 ##
##
def dodaj(a_list, b_list):
    global listaA, listaB
    for liczba in a_list:
        if liczba % 2 == 0:
            listaA = a_list

    for liczba2 in b_list:
        if liczba2 % 2 != 0:
            listaB = b_list

    polaczone = listaA + listaB
    return polaczone

##
## 2 ##
##
def slownik(data_text):
    return dict([("dlugosc tekstu", data_text.length), ("letters", data_text.index("D", "o", "g")), ("big_letters", data_text.upper()), ("small_letters", data_text.lower())])

##
## 3 ##
##
def funkcjaa(text, letter):
    lista = [x for x in text if x != letter]
    return lista
##
## 4 ##
##
def przeliczanie():
    print(" 1  Celsjusza\n 2 Fahrenheita\n 3 Kelvina\n 4 Rankine")
    temperature_type = input('''''')
    if temperature_type == ("1"):
        temp = int(input('''\nCelsjusza\n'''))
        print(temp)
    elif temperature_type == ("2"):
        temp = int(input('''\nFahrenheita\n'''))
        fahrenheit = temp * (9.0 / 5.0) + 32
        print(fahrenheit)
    elif temperature_type == ("3"):
        temp = int(input('''\nKelvina\n'''))
        kelvin = temp + 273.15
        print(kelvin)
    elif temperature_type == ("4"):
        temp = int(input('''\nRankine\n'''))
        rankine = (temp + 273.15) * (9.0 / 5.0)
        print(rankine)
    przeliczanie()
##
## 5 ##
##
class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def difference(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

##
## 6 ##
##
class ScienceCalculator(Calculator):
    def potega(self):
         return self.x ^ self.y


##
## 7 ##
##
def napisodtylu():
wyrazik = 'koteł'
print(wyrazik[::-1])

##
## 9 ##
##
import file_manager

print(file_manager.read_file())
print(file_manager.update_file())





