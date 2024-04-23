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

    #Szobák száma és ára random legenerálása (Őszintén nem akartam egyesével kitalálni nekik árakat és számokat, ezért random)
    egyagyasSzobak = []
    szobaszamok = []
    for i in range(0,8):
        r_ar = random.randint(10000,100000)
        r_szam = random.randint(100,999)
        while r_szam in szobaszamok:
            r_szam = random.randint(100,999)
        szobaszamok.append(r_szam)
        egyagyasSzobak.append(EgyagyasSzoba(r_ar,r_szam))

    ketagyasSzobak = []
    for i in range(0,8):
        r_ar = random.randint(10000,100000)
        r_szam = random.randint(100,999)
        while r_szam in szobaszamok:
            r_szam = random.randint(100,999)
        szobaszamok.append(r_szam)
        ketagyasSzobak.append(KetagyasSzoba(r_ar,r_szam))


    #Különlegességek hozzáadása random (Itt se akartam mindegyiknek megadni egyesével, szóval random)
    for i in range(0,len(egyagyasSzobak)):
        voltak = []
        for j in range(0,5):
            r = random.randint(0,len(kulonlegessegek)-1)
            while kulonlegessegek[r] in voltak:
                r = random.randint(0,len(kulonlegessegek)-1)
            egyagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[r])
            voltak.append(kulonlegessegek[r])

    for i in range(0,len(ketagyasSzobak)):
        voltak = []
        for j in range(0,5):
            r = random.randint(0,len(kulonlegessegek)-1)
            while kulonlegessegek[r] in voltak:
                r = random.randint(0,len(kulonlegessegek)-1)
            ketagyasSzobak[i].kulonlegesseg.append(kulonlegessegek[r])
            voltak.append(kulonlegessegek[r])

    #Képek hozzárendelése a szobákhoz (random)
    numlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    for i in range(0,len(egyagyasSzobak)):
        r = random.randint(0,len(numlist)-1)
        egyagyasSzobak[i].picture = pics[numlist[r]-1]
        numlist.pop(r)
    for i in range(0,len(ketagyasSzobak)):
        r = random.randint(0,len(numlist)-1)
        ketagyasSzobak[i].picture = pics[numlist[r]-1]
        numlist.pop(r)

    #Random értékelés hozzáadása
    for i in range(0,len(egyagyasSzobak)):
        r1 = random.randint(7,9)
        r2 = random.randint(0,9)
        egyagyasSzobak[i].rating = f"{r1}.{r2}"
        r3 = random.randint(1000,3000)
        egyagyasSzobak[i].rating_num = r3
    for i in range(0,len(ketagyasSzobak)):
        r1 = random.randint(7,9)
        r2 = random.randint(0,9)
        ketagyasSzobak[i].rating = f"{r1}.{r2}"
        r3 = random.randint(1000,3000)
        ketagyasSzobak[i].rating_num = r3

    #Szállodákhoz szobák rendelése
    szallodak = []
    szallodak.append(Szalloda("Generus Hotel"))
    szallodak.append(Szalloda("Crystal Cove Resort & Spa"))
    szallodak.append(Szalloda("The One Star Motel"))
    szallodak.append(Szalloda("Margaret Island Hotel"))

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

    #Szállodákhoz tartozó koordináta
    szallodak[0].x_cor = 46.9171
    szallodak[0].y_cor = 18.0716
    szallodak[1].x_cor = 46.6703
    szallodak[1].y_cor = 21.0842
    szallodak[2].x_cor = 48.1036
    szallodak[2].y_cor = 20.7746
    szallodak[3].x_cor = 47.3809
    szallodak[3].y_cor = 19.2157

    #Random foglalások létrehozása
    foglalasok = []
    for szn in range(0,4):
        for rn in range(0,4):
            fidopontok = []
            for fn in range(0,10):
                rm = random.randint(datetime.now().month,datetime.now().month+2)
                rd = random.randint(1,30)
                while (rm == datetime.now().month and rd <= datetime.now().day) or datetime(2024,rm,rd) in fidopontok:
                    rm = random.randint(datetime.now().month,datetime.now().month+2)
                    rd = random.randint(1,30)
                fidopontok.append(datetime(2024,rm,rd))
                foglalasok.append(Foglalas(datetime(2024,rm,rd),szallodak[szn],szallodak[szn].szobak[rn].szobaszam))


    return egyagyasSzobak, ketagyasSzobak, szallodak, foglalasok
print("kesz")