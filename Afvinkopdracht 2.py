#1
#Dit laat persoonlijke informatie zien door het gebruik vaan een string en /n om het overzichtelijk laten lijken
personalinfo = ("Yorick Cleijsen \nSirtemalaan 16, Grave Noord-Brabant, 5361 JZ \n06-37384074 \nBio-Informatics")
print(personalinfo)

print("////////////////////////////////////////////////////////////////")

#2
#Door het gebruik van input en een simpele berekening kun je de profit uitrekenen
predicted_sales = input("Enter predicted sales")
profit = float(predicted_sales) * float("0.23")
print(profit)

print("////////////////////////////////////////////////////////////////")

#4 
#Vull de prijzen van de items is
item1 = input("Enter prize of item 1")
item2 = input("Enter prize of item 2")
item3 = input("Enter prize of item 3")
item4 = input("Enter prize of item 4")
item5 = input("Enter prize of item 5")

#Voeg de Tax toe van 7%
Item1 = float(item1) * float(0.07)
Item2 = float(item2) * float(0.07)
Item3 = float(item3) * float(0.07)
Item4 = float(item4) * float(0.07)
Item5 = float(item5) * float(0.07)

#Subtotaal berekenen door alle items bij elkaar te voegen
subtotal = float(item1) + float(item2) + float(item3) + float(item4) + float(item5)
print("subtotal")
print(subtotal)

#Totale tax op de items wordt berekent door de Items (met een hoofdletter) bij elkaar toe te voegen
tax = float(Item1) + float(Item2) + float(Item3) + float(Item4) + float(Item5)
print("tax")
print(tax)

#totaal is tax + subtotaal voor het totaal
total = float(tax) + float(subtotal)
print("total")
print(total)

print("////////////////////////////////////////////////////////////////")

#5
#Kun je zelf berekene  wat je afstand is
speed = int(input("Enter you driving speed in miles per hour"))
time = int(input("Enter your estimated driving time"))
distance = speed * time
print(distance)

#De vaste afstanden voor 6, 10 en 15 uur
print("Distance travels after '6' hours")
milesI = float("70") * float("6")
print(milesI)

print("Distance travels after '10' hours")
milesII = float("70") * float("10")
print(milesII)

print("Distance travels after '15' hours")
milesIII = float("70") * float("15")
print(milesIII)

print("////////////////////////////////////////////////////////////////")

#7
#Simpele berekening dat gebruikt maar van input om je Miles Per Gallon the berekenen
miles_driven = int(input("Enter your driven miles"))
gog = int(input("Enter your amount of gallons used"))
MPG = miles_driven / gog
print(MPG)

print("////////////////////////////////////////////////////////////////")

#10
#Bereken hoeveel cups van ingredienten je nodig hebt voor 1 cookie
S = float(1.5) / float(48)
B = float(1) / float(48)
F = float(2.75) / float(48)

cookie = input("How many cookies would you like to make?")
#berekening hoeveel cups je nodig hebt voor het aantal ingevoerde cookies
totalS = float(S) * float(cookie)
totalB = float(B) * float(cookie)
totalF = float(F) * float(cookie)

#Print van hoeveel cups ingredienten je nodig hebt per ingredient
print("You will need the following for your selected amount of cookies")
print("cups of sugar")
print(totalS)
print("cups of butter")
print(totalB)
print("cups of flour")
print(totalF)

