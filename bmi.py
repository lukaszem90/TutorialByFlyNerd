print("Hej. witaj w kalkulatorze BMI!")
print("Ok mi swoją wagę?")
waga=float(input())
print("Podasz mi swój wzrost")
wzrost=float(input())/100
print("Ok. dzieki. liczę!")
BMI=waga / (wzrost ** 2)
print("Twoje bmi wynosi:",round(BMI,2))

if (BMI<18.5): 
    print("Masz niedowagę")
elif (18.5<BMI<=24): 
    print("Waga normalna")
elif (24<BMI<=26.5): 
    print("Lekka nadwaga")

else: 
    print("Nadwaga!")
    if (30>=BMI>35):
        print("Otyłość I stopnia")
    elif (35>=BMI>40):
        print("Otyłość II stopnia")
    elif (BMI>40):
        print("Otyłość III stopnia")






#Niedowaga	< 18.5
#Waga normalna	18.5 – 24
#Lekka nadwaga	24 – 26.5
#Nadwaga	> 26.5
#Otyłość I stopnia	30 – 35
#Otyłość II stopnia	30 – 40
#Otyłość III stopnia	> 40