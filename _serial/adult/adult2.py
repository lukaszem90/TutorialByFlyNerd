# -*- coding: utf8 -*-

print("Ile masz lat?")
age = int(input())
n_age = 18 - age
#newage=18-input(int(age))
#print(newage)
if (age>=18):
    print("Hurra, juz dawno po osiemnastce!")
elif (age >100):
    print("♫ 200 lat ♫")
else:
    print ("Użytkkownik niepełnoletni")
    print ("Zgłos sie za", n_age, "lat")