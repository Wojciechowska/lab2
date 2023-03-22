#zad1
#a)
import math
a = math.exp(10)
print(a)

#b)
b = (math.log(5 + math.sin(8) ** 2)) ** (1/6)
print(b)

#c)
c = math.floor(3.55)
print(c)

#d)
d = math.ceil(4.80)
print(d)

#zad2
imie = 'AGATA'
nazwisko = 'WOJCIECHOWSKA'
x = imie.capitalize() + ' ' + nazwisko.capitalize()
print(x)

#zad3
e = 'testowy la la la lala tekst'
f = e.count('la')
print(f)

#zad4
g = 'test;jymyyjyjyjyjjjjjowy'
print(g[1])
print(g[len(g)-1]) #lub print(g[-1])

#zad5
h = g.split('t')
print(h)

#zad6
tekst = 'zad6'
numer = 6.34758
szesnastkowy = 0xFF

print('Zmienna typu string: {}'.format(tekst))
print('Zmienna typu float: {:.2f}'.format(numer))
print('Zmienna typu hexadecimal: 0x{:X}'.format(szesnastkowy))

#zad7
sporty = ['pilka nozna', 'koszykowka', 'pilka reczna']
sporty.reverse()
print(sporty)
sporty.extend(['skok w dal', 'bieg na 100 metrow'])
print(sporty)

#zad8
slownik = {'cd.' : 'ciag dalszy', 'dr' : 'doktor', 'itp' : 'i tym podobne'}
print(slownik)

#zad9
gry = {'cs' : 'CounterStrike', 'wow' : 'World Of Warcraft', 'lol' : 'League Of Legends'}
ilosc_elementow = len(gry)
print(ilosc_elementow)

#zad10
print('Wpisz zdanie.')
zdanie = input()
print(zdanie + ' zawiera literę "a" ' + str(zdanie.count('a')) + ' razy.')


#zad11
liczba_pierwsza = input()
liczba_druga = input()
liczba_trzecia = input()

liczba_pierwsza = int(liczba_pierwsza)
liczba_druga = int(liczba_druga)
liczba_trzecia = int(liczba_trzecia)

if (liczba_pierwsza > liczba_druga) & (liczba_pierwsza > liczba_trzecia):
    print(str(liczba_pierwsza) + ' jest największa')
elif(liczba_druga > liczba_pierwsza) & (liczba_druga > liczba_trzecia):
    print(str(liczba_druga) + ' jest największa')
else:
    print(str(liczba_trzecia) + ' jest największa')


#zad12
lista_kwadrat = [2, 4, 12, 10.5, 50.32, 8.88]
print(lista_kwadrat)
for z in range(len(lista_kwadrat)):
    lista_kwadrat[z] = lista_kwadrat[z] ** 2
print(lista_kwadrat)


#zad13
print('Podaj 10 liczb')
liczby = []
i = 1
while i <= 10:
    m = int(input())
    if m % 2 == 0:
        liczby.append(m)
    i += 1
print(liczby)






