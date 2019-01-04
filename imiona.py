dict_names = {
    "Jan" : "męskie",
    "Adam" : "męskie",
    "Olek" : "męskie",
    "Kuba" : "męskie",
    "Wojtek" : "męskie",
    "Justyna" : "żeńskie",
    "Patrycja" : "żeńskie",
    "Faustyna" : "żeńskie",
    "Klaudia" : "żeńskie",
    "Paulina" : "żeńskie",
}

print ("Hej, to nasza lista imion:")
print (list(dict_names.keys()))
name=(input("Podaj imie:"))

if (name in list(dict_names.keys())):
    print (name,"to imię",dict_names[name])
else:
    print("Mamy problem!")
    gender=input("To imie męskie czy żeńskie? Wpisz m = męskie, f = żeńskie")
    if (gender == "f"):
        dict_names[name]="męskie"
    else:
        dict_names[name]="żeńskie"
print (list(dict_names.keys()))
print("Krzyzyk po prawej, dzieki!")



#by flynerd.pl