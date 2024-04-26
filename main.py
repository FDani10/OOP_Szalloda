from classes import Foglalas
from classes import MyCalendar
import tkinter as tk
from feltoltes import upload
from PIL import Image, ImageTk
import datetime
import tkintermapview
import ctypes


main = tk.Tk()
main.geometry("500x500")

egyagyasSzobak, ketagyasSzobak, szallodak, foglalasok = upload()

def login():
    if(username.get() != "" and password.get() != ""):
        felhasznalok_txt = open("./verysecret/felhasznalok.txt","r")
        felhasznalok_txt.readline()
        vanilyen = False
        for x in felhasznalok_txt:
            sorok = x.split(';')
            un = sorok[0]
            pw = sorok[1][:-1]
            if un == username.get() and pw == password.get():
                vanilyen = True
        if vanilyen == True:
            welcomeBack = tk.Label(canvas,bg="#41a0e8",text=f"Üdvözlünk újra, {username.get()}",font='Ariel 20 bold')
            welcomeBack.place(x=100,y=50,width=300,height=60)
            user_name_lbl.configure(text=username.get())
            main.after(3000,upTheCurtain)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Nem található ilyen felhasználó!", "Hiba!", 1)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Töltse ki az összes mezőt!", "Hiba!", 1)

def upTheCurtain():
    global block_y
    block_y -= 10
    canvas.place(x=0,y=block_y)
    main.after(10,upTheCurtain)

def chosenHotel(num):
    global room_1_name
    global room_2_name
    global room_3_name
    global room_4_name
    global roundedbutton1
    global roundedbutton2
    global roundedbutton3
    global roundedbutton4
    room_1_name.configure(text=f"Szobaszám: {szallodak[num].szobak[0].szobaszam}")
    room_2_name.configure(text=f"Szobaszám: {szallodak[num].szobak[1].szobaszam}")
    room_3_name.configure(text=f"Szobaszám: {szallodak[num].szobak[2].szobaszam}")
    room_4_name.configure(text=f"Szobaszám: {szallodak[num].szobak[3].szobaszam}")

    roundedbutton1.configure(image=szallodak[num].szobak[0].picture,command=lambda:chosenRoom(szallodak[num].szobak[0],szallodak[num]))
    roundedbutton2.configure(image=szallodak[num].szobak[1].picture,command=lambda:chosenRoom(szallodak[num].szobak[1],szallodak[num]))
    roundedbutton3.configure(image=szallodak[num].szobak[2].picture,command=lambda:chosenRoom(szallodak[num].szobak[2],szallodak[num]))
    roundedbutton4.configure(image=szallodak[num].szobak[3].picture,command=lambda:chosenRoom(szallodak[num].szobak[3],szallodak[num]))
    slideToTheLeft()

def slideToTheLeft():
    global c_x
    global c_x2
    global c_x3
    c_x -= 10
    c_x2 -= 10
    c_x3 -= 10
    canvas_2.place(x=c_x,y=0)
    canvas_3.place(x=c_x2,y=0)
    canvas_4.place(x=c_x3,y=0)
    if c_x2 != 0:
        main.after(10,slideToTheLeft)

def slideToTheRight():
    global c_x
    global c_x2
    global c_x3
    c_x3 += 10
    c_x2 += 10
    c_x += 10
    canvas_2.place(x=c_x,y=0)
    canvas_3.place(x=c_x2,y=0)
    canvas_4.place(x=c_x3,y=0)
    if c_x2 != 500:
        main.after(10,slideToTheRight)

def chosenRoom(room,hotel):
    x = hotel.x_cor
    y = hotel.y_cor
    map.set_position(x,y,marker=True)

    img.configure(image=room.picture)
    szobaszam.configure(text=f"Ár: {room.ar}/éjszaka")
    ert_2.configure(text=f"{room.rating}")
    ert_3.configure(text=f"({room.rating_num} értékelés)")

    kul1.configure(text=f"• {room.kulonlegesseg[0]}\n• {room.kulonlegesseg[1]}\n• {room.kulonlegesseg[2]}\n• {room.kulonlegesseg[3]}\n• {room.kulonlegesseg[4]}")

    global cal
    cal.place_forget()

    cal = MyCalendar(canvas_4, selectmode='day',
                 year=2024, month=4, disableddaybackground="gray",
                 day=19)
    
    for i in range(0,len(foglalasok)):
        if foglalasok[i].szobaszam == room.szobaszam:
            cal.disable_date(datetime.date(foglalasok[i].idopont.year, foglalasok[i].idopont.month, foglalasok[i].idopont.day))
    cal.place(x=240,y=224)

    btn_fog.configure(command=lambda:dateSelectedVerifier(hotel,room))
    slideLeftRoom()

def slideLeftRoom():
    global c_x
    global c_x2
    global c_x3
    c_x -= 10
    c_x2 -= 10
    c_x3 -= 10
    canvas_2.place(x=c_x,y=0)
    canvas_3.place(x=c_x2,y=0)
    canvas_4.place(x=c_x3,y=0)
    if c_x3 != 0:
        main.after(10,slideLeftRoom)

def slideRightRoom():
    global c_x
    global c_x2
    global c_x3
    c_x3 += 10
    c_x2 += 10
    c_x += 10
    canvas_2.place(x=c_x,y=0)
    canvas_3.place(x=c_x2,y=0)
    canvas_4.place(x=c_x3,y=0)
    if c_x3 != 500:
        main.after(10,slideRightRoom)

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

def dateSelectedVerifier(hotel, room):
    date = cal.get_date().split('/')
    caldate = datetime.datetime(int(date[2])+2000,int(date[0]),int(date[1]))
    if to_integer(caldate) > to_integer(datetime.datetime.now()):
        cal.disable_date(datetime.date(caldate.year, caldate.month, caldate.day))
        foglalasok.append(Foglalas(datetime.datetime(caldate.year,caldate.month,caldate.day),hotel,room.szobaszam,username.get()))
        slideRightRoom()
        ctypes.windll.user32.MessageBoxW(0, "Sikeresen lefoglalta a szobát!", "Siker!", 1)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Nem lehetséges előző/mai dátumra foglalni!", "Hiba!", 1)

def getProfilePage():
    global c_x
    global c_x2
    global c_x3
    global c_x4
    c_x4 +=10
    c_x3 += 10
    c_x2 += 10
    c_x += 10
    canvas_2.place(x=c_x,y=0)
    canvas_3.place(x=c_x2,y=0)
    canvas_4.place(x=c_x3,y=0)
    canvas_5.place(x=c_x4,y=0)
    if c_x4 != 0:
        main.after(10,getProfilePage)

#region Szállodák képernyő
canvas_2 = tk.Canvas(main,bg="#8abee6",width=500,height=500)
canvas_2.place(x=0,y=0)
hotel_kiv = tk.Label(canvas_2,bg="#8abee6",text="Válasszon hotelt",font='Helvetica 25 bold italic')
hotel_kiv.place(x=100,y=20,width=300,height=60)

image_p=Image.open('./pics/profpicround.jpg')
img_p=image_p.resize((60, 60))
my_img_p=ImageTk.PhotoImage(img_p)
user_btn = tk.Button(canvas_2, image=my_img_p, command=getProfilePage)
user_btn["bg"] = "#8abee6"
user_btn["activebackground"] = "#8abee6"
user_btn["border"] = "0"
user_btn.place(x=420,y=10,width=60,height=60)

user_name_lbl = tk.Label(canvas_2,bg="#8abee6",justify="center")
user_name_lbl.place(x=430,y=70)

image=Image.open('./pics/onestar-modified.png')
img=image.resize((207, 152))
my_img=ImageTk.PhotoImage(img)
roundedbutton = tk.Button(canvas_2, image=my_img, command=lambda: chosenHotel(0))
roundedbutton["bg"] = "#8abee6"
roundedbutton["activebackground"] = "#8abee6"
roundedbutton["border"] = "0"
roundedbutton.place(x=30,y=100, width=207,height=152)

hotel_1_name = tk.Label(canvas_2,text=szallodak[0].nev,font='Arial 12 italic',bg="#8abee6")
hotel_1_name.place(x=70,y=255)


image=Image.open('./pics/hotel1.jpg')
img=image.resize((207, 152))
my_img2=ImageTk.PhotoImage(img)
roundedbutton = tk.Button(canvas_2, image=my_img2, command=lambda: chosenHotel(1))
roundedbutton["bg"] = "#8abee6"
roundedbutton["activebackground"] = "#8abee6"
roundedbutton["border"] = "0"
roundedbutton.place(x=270,y=100, width=207,height=152)

hotel_1_name = tk.Label(canvas_2,text=szallodak[1].nev,font='Arial 12 italic',bg="#8abee6")
hotel_1_name.place(x=330,y=255)


image=Image.open('./pics/hotel2.jpg')
img=image.resize((207, 152))
my_img3=ImageTk.PhotoImage(img)
roundedbutton = tk.Button(canvas_2, image=my_img3, command=lambda: chosenHotel(2))
roundedbutton["bg"] = "#8abee6"
roundedbutton["activebackground"] = "#8abee6"
roundedbutton["border"] = "0"
roundedbutton.place(x=30,y=300, width=207,height=152)

hotel_1_name = tk.Label(canvas_2,text=szallodak[2].nev,font='Arial 12 italic',bg="#8abee6")
hotel_1_name.place(x=70,y=455)


image=Image.open('./pics/hotel3.jpg')
img=image.resize((207, 152))
my_img4=ImageTk.PhotoImage(img)
roundedbutton = tk.Button(canvas_2, image=my_img4, command=lambda: chosenHotel(3))
roundedbutton["bg"] = "#8abee6"
roundedbutton["activebackground"] = "#8abee6"
roundedbutton["border"] = "0"
roundedbutton.place(x=270,y=300, width=207,height=152)

hotel_1_name = tk.Label(canvas_2,text=szallodak[3].nev,font='Arial 12 italic',bg="#8abee6")
hotel_1_name.place(x=320,y=455)
#endregion

#region Kiválasztott hotel képernyő
c_x=0
c_x2=500

canvas_3 = tk.Canvas(main,bg="#8abee6",width=500,height=500)
canvas_3.place(x=500,y=0)

image=Image.open('./pics/onestar-modified.png')
img=image.resize((207, 152))
my_img5=ImageTk.PhotoImage(img)
roundedbutton1 = tk.Button(canvas_3, image=my_img5, command=lambda: chosenRoom(0))
roundedbutton1["bg"] = "#8abee6"
roundedbutton1["activebackground"] = "#8abee6"
roundedbutton1["border"] = "0"
roundedbutton1.place(x=30,y=100, width=207,height=152)

room_1_name = tk.Label(canvas_3,text="",font='Arial 12 italic',bg="#8abee6")
room_1_name.place(x=60,y=255)


image=Image.open('./pics/onestar-modified.png')
img=image.resize((207, 152))
my_img6=ImageTk.PhotoImage(img)
roundedbutton2 = tk.Button(canvas_3, image=my_img6, command=lambda: chosenRoom(1))
roundedbutton2["bg"] = "#8abee6"
roundedbutton2["activebackground"] = "#8abee6"
roundedbutton2["border"] = "0"
roundedbutton2.place(x=270,y=100, width=207,height=152)

room_2_name = tk.Label(canvas_3,text="",font='Arial 12 italic',bg="#8abee6")
room_2_name.place(x=300,y=255)


image=Image.open('./pics/onestar-modified.png')
img=image.resize((207, 152))
my_img7=ImageTk.PhotoImage(img)
roundedbutton3 = tk.Button(canvas_3, image=my_img7, command=lambda: chosenRoom(2))
roundedbutton3["bg"] = "#8abee6"
roundedbutton3["activebackground"] = "#8abee6"
roundedbutton3["border"] = "0"
roundedbutton3.place(x=30,y=300, width=207,height=152)

room_3_name = tk.Label(canvas_3,text="",font='Arial 12 italic',bg="#8abee6")
room_3_name.place(x=60,y=455)


image=Image.open('./pics/onestar-modified.png')
img=image.resize((207, 152))
my_img8=ImageTk.PhotoImage(img)
roundedbutton4 = tk.Button(canvas_3, image=my_img8, command=lambda: chosenRoom(3))
roundedbutton4["bg"] = "#8abee6"
roundedbutton4["activebackground"] = "#8abee6"
roundedbutton4["border"] = "0"
roundedbutton4.place(x=270,y=300, width=207,height=152)

room_4_name = tk.Label(canvas_3,text="",font='Arial 12 italic',bg="#8abee6")
room_4_name.place(x=300,y=455)

btn_c3 = tk.Button(canvas_3,text="VISSZA", command=slideToTheRight)
btn_c3.place(x=200,y=400)
#endregion

#region Kiválasztott szoba képernyő
c_x3 = 1000
canvas_4 = tk.Canvas(main,bg="#8abee6",width=500,height=500)
canvas_4.place(x=1000,y=0)

label = tk.LabelFrame(canvas_4)
label.place(x=31,y=240,width=190,height=190)

map = tkintermapview.TkinterMapView(label,width=190,height=190)
map.set_position(47.3809,19.2157,marker=True)
map.set_zoom(15)
map.place(x=0,y=0)

cal = MyCalendar(canvas_4, selectmode='day',
                 year=2024, month=4, disableddaybackground="gray",
                 day=19)
cal.place(x=240,y=224)

btn2 = tk.Button(canvas_4,text="Vissza",command=slideRightRoom)
btn2.place(x=60,y=440,width=135,height=40)

btn_fog = tk.Button(canvas_4,text="FOGLALÁS",command=dateSelectedVerifier)
btn_fog.place(x=240,y=414,width=250,height=66)

img = tk.Label(canvas_4,image=my_img)
img.place(x=28,y=20,width=245,height=184)
szobaszam = tk.Label(canvas_4,text="Szobaszám: 420",font="Ariel 13 bold",bg="#8abee6")
szobaszam.place(x=65,y=209,width=160,height=31)

ert_1 = tk.Label(canvas_4,text="Értékelés:",bg="#8abee6",font="Ariel 12 bold")
ert_2 = tk.Label(canvas_4,text="8.4",bg="#8abee6",font="Ariel 14 bold")
ert_3 = tk.Label(canvas_4,text="(1254 értékelés)",bg="#8abee6",font="Ariel 10 bold")
ert_1.place(x=337,y=10)
ert_2.place(x=357,y=30)
ert_3.place(x=325,y=54)

kul = tk.Label(canvas_4,text="Különlegességek:",bg="#8abee6",font="Ariel 12")
kul1 = tk.Label(canvas_4,text="• WC\n• Terasz\n• Kilátás\n• Hangszigetelt ablakok\n• Minibár",bg="#8abee6",font="Ariel 12 italic")
kul.place(x=320,y=85)
kul1.place(x=278,y=106,width=200,height=110)
#endregion

#region Saját fiók képernyő
c_x4 = -500
canvas_5 = tk.Canvas(main,bg="#8abee6",width=500,height=500)
canvas_5.place(x=-500,y=0)

button_prof_back = tk.Button(canvas_5,text="Vissza",command=login)
button_prof_back.place(x=150,y=320,width=200,height=30)

#endregion

#region Belépő képernyő
block_y=0
canvas = tk.Canvas(main,bg="#41a0e8",width=500,height=500)
canvas.place(x=0,y=0)

koszonto = tk.Label(canvas,bg="#41a0e8",text="SZOBAFOGLALÓ",font='Helvetica 25 bold italic')
koszonto.place(x=100,y=100,width=300,height=60)

username_ph = tk.Label(canvas,bg="#41a0e8",text="Felhasználónév:",font='Arial 12 italic')
username_ph.place(x=110,y=180,width=200,height=20)
username = tk.Entry(canvas)
username.place(x=150,y=200,width=200,height=30)

password_ph = tk.Label(canvas,bg="#41a0e8",text="Jelszó:",font='Arial 12 italic')
password_ph.place(x=75,y=240,width=200,height=20)
password = tk.Entry(canvas,show="*")
password.place(x=150,y=260,width=200,height=30)

button = tk.Button(canvas,text="Belépés",command=login)
button.place(x=150,y=320,width=200,height=30)
#endregion


main.mainloop()