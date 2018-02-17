#!/usr/bin/python
print "Ala ma kota"

import os

ilosc=0
for linie in file("lorem.txt"):
    if linie.find("bash")+1:
        ilosc=ilosc+1
print ilosc

import re
liczba=0
for linie in file("lorem.txt"):
    if re.search("[0-9]+", linie):
        liczba=liczba+1
print liczba

ilosc_linii=0
for linie in file("lorem.txt"):
    if len(linie)==80:
        print linie
        ilosc_linii=ilosc_linii+1
print ilosc_linii

if os.path.exists('lorem.txt'):
    print "Istnieje"
else:
    print "Nie istnieje"

if os.path.exists('lorem2.txt'):
    print "Istnieje"
else:
    print "Nie istnieje"
