import copy
##
## 1 ##
##
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
##
## 2 ##
##
liczba_liter1 = tekst.count("a")
liczba_liter2 = tekst.count("b")
print(f"W tekście jest {liczba_liter1}liter A oraz {liczba_liter2}liter B")
imie = "Damian"
nazwisko = "Trzciński"
litera_1 = "A"
litera_2 = "B"
litera_1 = imie[2]
litera_2 = nazwisko[3]
##
## 3 ##
##
class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

print('%s %r' % (Data(), Data()))
print('{0!s} {0!r}'.format(Data()))

print('%10s' % ('test',))
print('{:>10}'.format('test'))

print('%-10s' % ('test',))
print('{:10}'.format('test'))


print('%d' % (42,))
print('{:d}'.format(42))


print('%.5s' % ('xylophone',))
print('{:.5}'.format('xylophone'))

##
## 4 ##
##
zmienna_typu_string = "abdfsdasdawsd"
print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize())
##
## 5 ##
##
print(imie[::-1] +" "+ nazwisko[::-1])
##
## 6 ##
##
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista[5:]
lista = lista[:5]
print(lista)
print(lista2)
##
## 7 ##
##
polaczone = lista + lista2
print(polaczone)
polaczone.append('0')
print(polaczone)
kopia = copy.copy(polaczone)
print(kopia)

## malejaco = polaczone.sort()
## print(malejaco)

##
## 8 ##
##
krotka1 = (111111, "Damian", "Mróz")
krotka2 = (222222, "Damian", "Śnieg")
krotka3 = (333333, "Eryk", "Kowalski")
krotka4 = (444444, "Tymek", "Kowal")
##
## 9 ##
##
krotka1s = {'index': '111111', 'imie': 'Damian', 'nazwisko': 'Mróz'}
krotka2s = {'index': '222222', 'imie': 'Damian', 'nazwisko': 'Śnieg'}
krotka3s = {'index': '333333', 'imie': 'Eryk', 'nazwisko': 'Kowalski'}
krotka4s = {'index': '444444', 'imie': 'Tymek', 'nazwisko': 'Kowal'}
krotka1s['wiek'] = '21'
krotka1s['mail'] = 'mojmail@gmail.com'
krotka1s['rok_urodzenia'] = '01.01.1998'
krotka1s['adres'] = 'Olsztyn'

krotka2s['wiek'] = '23'
krotka2s['mail'] = 'mojmail@gmail.com'
krotka2s['rok_urodzenia'] = '01.01.1998'
krotka2s['adres'] = 'Olsztyn'

krotka3s['wiek'] = '22'
krotka3s['mail'] = 'mojmail@gmail.com'
krotka3s['rok_urodzenia'] = '01.01.1998'
krotka3s['adres'] = 'Olsztyn'

krotka4s['wiek'] = '20'
krotka4s['mail'] = 'mojmail@gmail.com'
krotka4s['rok_urodzenia'] = '01.01.1998'
krotka4s['adres'] = 'Olsztyn'
print(krotka1s)
print(krotka1s.keys())
print(krotka1s.values())
##
## 10 ##
##
telefony = [111111111, 111111111, 999888777, 999888777, 777888999, 777888999, 999999999, 888888888, 777777777]
telefonybez = set(telefony)
print(telefonybez)
##
## 11 ##
##
lista = list(range(10))
print(lista)
##
## 12 ##
##
for a in range(100, 20, -5):
    print(a)
##
## 13 ##
##


