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




