#Nem akartam, hogy a main.py-ben egy csomó sort elvegyen ez, szóval külön fájlt csináltam neki

from classes import EgyagyasSzoba
from classes import KetagyasSzoba
from classes import Szalloda
from classes import Foglalas
import random
from random import randrange
from datetime import timedelta
from datetime import datetime
from imageResizer import picSizer

#Feltöltés
def upload():
    kulonlegessegek = [
    "Kényelmes ágy",
    "Tiszta ágynemű és párnák",
    "Légkondicionáló",
    "Fürdőszoba",
    "Törölközők",
    "Hajszárító",
    "TV",
    "Ingyenes Wi-Fi",
    "Íróasztal és szék",
    "Minibár",
    "Széf",
    "Telefon",
    "Piperecikkek",
    "Központi világítás",
    "Szobaszerviz",
    "Vasaló és vasalódeszka",
    "Hangszigetelt ablakok",
    "Kilátás",
    "Reggeli lehetőség",
    "Vendégkiszolgálás"]

    pics = picSizer()

    #Egyágyas szobák, és kétágyas szobák beolvasása .txt fileból (id, szobaszám, ár, értékelés, értékelés_szám, különlegességek)
    i = 0
    egyagyasSzobak = []
    egyagyas_txt = open("./verysecret/egyagyas.txt", "r")
    egyagyas_txt.readline()
    for line in egyagyas_txt:
        sorok = line.split(';')
        egyagyasSzobak.append(EgyagyasSzoba(sorok[0],sorok[3],sorok[2]))
        egyagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[6])])
        egyagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[7])])
        egyagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[8])])
        egyagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[9])])
        egyagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[10])])
        egyagyasSzobak[i].rating = str(sorok[4])
        egyagyasSzobak[i].rating_num = str(sorok[5])
        i = i + 1
    egyagyas_txt.close()

    i = 0
    ketagyasSzobak = []
    ketagyas_txt = open("./verysecret/ketagyas.txt", "r")
    ketagyas_txt.readline()
    for line in ketagyas_txt:
        sorok = line.split(';')
        ketagyasSzobak.append(KetagyasSzoba(sorok[0],sorok[3],sorok[2]))
        ketagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[6])])
        ketagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[7])])
        ketagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[8])])
        ketagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[9])])
        ketagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[int(sorok[10])])
        ketagyasSzobak[i].rating = str(sorok[4])
        ketagyasSzobak[i].rating_num = str(sorok[5])
        i = i + 1
    ketagyas_txt.close()

    #Képek hozzárendelése a szobákhoz
    for i in range(0,len(egyagyasSzobak)):
        egyagyasSzobak[i].picture = pics[i]
    for i in range(0,len(ketagyasSzobak)):
        ketagyasSzobak[i].picture = pics[i+8]

    #Szállodák beolvasása txt fileból, és szobák rendelése hozzájuk
    szallodak = []
    ketagyas_txt = open("./verysecret/szalloda.txt", "r")
    ketagyas_txt.readline()
    for line in ketagyas_txt:
        sorok = line.split(';')
        szallodak.append(Szalloda(sorok[0],sorok[1],float(sorok[2]),float(sorok[3])))

    szallodak[0].szobak.append(egyagyasSzobak[0])
    szallodak[0].szobak.append(egyagyasSzobak[1])
    szallodak[0].szobak.append(ketagyasSzobak[0])
    szallodak[0].szobak.append(ketagyasSzobak[1])

    szallodak[1].szobak.append(egyagyasSzobak[2])
    szallodak[1].szobak.append(egyagyasSzobak[3])
    szallodak[1].szobak.append(ketagyasSzobak[2])
    szallodak[1].szobak.append(ketagyasSzobak[3])

    szallodak[2].szobak.append(egyagyasSzobak[4])
    szallodak[2].szobak.append(egyagyasSzobak[5])
    szallodak[2].szobak.append(ketagyasSzobak[4])
    szallodak[2].szobak.append(ketagyasSzobak[5])

    szallodak[3].szobak.append(egyagyasSzobak[6])
    szallodak[3].szobak.append(egyagyasSzobak[7])
    szallodak[3].szobak.append(ketagyasSzobak[6])
    szallodak[3].szobak.append(ketagyasSzobak[7])

    #Foglalások beolvasása txt fájlból
    foglalasok = []
    foglalas_txt = open("./verysecret/foglalas.txt", "r")
    foglalas_txt.readline()
    for line in foglalas_txt:
        sorok = line.split(';')
        date_sor = sorok[0].split('-')
        foglalasok.append(Foglalas(datetime(int(date_sor[0]),int(date_sor[1]),int(date_sor[2])),szallodak[int(sorok[1])-1],sorok[2],sorok[3][:-1]))

    return egyagyasSzobak, ketagyasSzobak, szallodak, foglalasok