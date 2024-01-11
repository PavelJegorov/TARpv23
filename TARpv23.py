#from importlib.resources import Package
#from random import *
#from tkinter import Pack
#10
#P=randint(1,5)
#hind=12.90
#hind*=1.1 #hind koos jätatega
#osa=round(hind/P,2)
#print("Iga sõber maksab: ",osa)


#print("Tere maailm!")
#nimi=input("Mis on simu nimi?")
#vanus=int(input("Kui vana sa oled")) #floae()->2.5
#print("Tere tulemast! "+nimi". Sa oled"+str(vanus)+" aasta vana")
#print("Tere tulemast! ",nimi,". Sa oled",vanus,"aasta vana")
#print("Tere tulemast! {0} Sa oled {1} aastat vana".format(nimi,vanus))
#print("Muutuja vanus=",vanus,",tüüp on "(type(vanus))

#2
#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis = True

#print("Muutuja vanus=",vanus,",tüüp on",type(vanus))
#print("Muutuja eesnimi=",eesnimi,",tüüp on ",type(eesnimi))
#print("Muutuja pikkus=",pikkus,",tüüp on ",type(pikkus))
#print("Muutuja kas_käib_koolis=",kas_käib_koolis,",tüüp on ",type(kas_käib_koolis))

#3
#from random import *
#kokku=randint(10,100)
#print("Kokku: ", kokku)
#mitu=int(input("mitu kommi tahab võtta?"))
#kokku=mitu
#print("Nüüd laua peal on",kokku,"kommid")


#6
try:
    aeg = float(input("Mitu tundi kulus sõiduks")) #aeg ie saa olla 0
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus/aeg
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except :
    print("Viga andmetüübiga")

print()

#4
puu = float(input("Напиши длину окружности дерева"))
läbimõõt = 