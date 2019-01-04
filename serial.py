# -*- coding: utf8 -*-
#tutorial by flynerdpl
#dodaje, by github ożył w moim postanowieniu :)

serials={
    'tytul 1' : 2,
    'tytul 2' : 3,
    'tytul 3' : 5,
    'tytul 4' : 6,
    'tytul 5' : 4,
    'tytul 6' : 1,
    'tytul 7' : 4,
    'tytul 8' : 5,
    }

print(list(serials.keys()))
name=(input("Jaki serial chcesz obejrzec?"))
print('*'*40)
print("Serial {} otrzymał ocenę: {}".format(name,serials[name]))
name2=(input("Czy dodajemy film do bazy?"))
rating = (input("Jaka ocene otrzymal "+name2+" ?"))
serials[name2] = float(rating)
print("v"*40)
print(list(serials.keys()))
print ("Ok")
print("Żegnam w zupdateowanym pliku!")