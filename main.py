from classes import Foglalas
from classes import MyCalendar
from classes import Felhasznalo
import tkinter as tk
from feltoltes import upload
from PIL import Image, ImageTk
import datetime
import tkintermapview
import ctypes


main = tk.Tk()
main.geometry("500x500")

egyagyasSzobak, ketagyasSzobak, szallodak, foglalasok, felhasznalok = upload()

def login():
    if(username.get() != "" and password.get() != ""):
        vanilyen = False
        for x in range(0,len(felhasznalok)):
            un = felhasznalok[x].username
            pw = felhasznalok[x].password
            if un == username.get() and pw == password.get():
                vanilyen = True
        if vanilyen == True:
            welcomeBack = tk.Label(canvas,bg="#2694E8",text=f"Üdvözlünk újra, {username.get()}",font='Ariel 15 bold',fg="white")
            welcomeBack.place(x=100,y=140,width=300,height=40)
            user_name_lbl.configure(text=username.get())
            main.after(3000,upTheCurtain)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Nem található ilyen felhasználó!", "Hiba!", 0)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Töltse ki az összes mezőt!", "Hiba!", 0)

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

        f = open("./verysecret/foglalas.txt", "a")
        f.write(f"{caldate.year}-{caldate.month}-{caldate.day};{hotel.id};{room.szobaszam};{username.get()};\n")
        f.close()

        slideRightRoom()
        ctypes.windll.user32.MessageBoxW(0, "Sikeresen lefoglalta a szobát!", "Siker!", 0)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Nem lehetséges előző/mai dátumra foglalni!", "Hiba!", 0)

def doProfilePage():
    global v
    global t
    v.destroy()
    t.destroy()

    v = tk.Scrollbar(canvas_foglist)
    v.pack(side = "right", fill = "y")
    t = tk.Text(canvas_foglist, width = 30, height = 17, wrap = "none",
    yscrollcommand = v.set,bg="#8abee6")
    label_nev.config(text=username.get())
    van_ilyen = False
    for i in range(0,len(foglalasok)):
        if foglalasok[i].foglalo_nev == username.get():
            btn_lemond = tk.Button(t,text="Lemondás",command=lambda e = foglalasok[i]:lemondas(e))
            van_ilyen = True
            ar = 0
            for j in range(0,len(foglalasok[i].szalloda.szobak)):
                if foglalasok[i].szalloda.szobak[j].szobaszam == foglalasok[i].szobaszam:
                    ar = foglalasok[i].szalloda.szobak[j].ar
            t.insert("end",f"{foglalasok[i].szalloda.nev} | {foglalasok[i].szobaszam} | {foglalasok[i].idopont.year}-{foglalasok[i].idopont.month}-{foglalasok[i].idopont.day} | {ar} Ft | ")
            t.window_create("end", window=btn_lemond)
            t.insert("end", "\n")
            t.insert("end","\n")
    if van_ilyen == False:
        t.config(font="Ariel 15")
        t.insert("end",f"Nem található foglalás a fiókjához!")

    t.tag_configure("center", justify='center')
    t.tag_add("center", 1.0, "end")
    t.config(state="disabled")
    t.pack(side="top", fill="x")

    v.config(command=t.yview)
    getProfilePage()

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

def SlideBackProfile():
    global c_x
    global c_x2
    global c_x3
    global c_x4
    c_x4 -=10
    c_x3 -= 10
    c_x2 -= 10
    c_x -= 10
    canvas_2.place(x=c_x,y=0)
    canvas_3.place(x=c_x2,y=0)
    canvas_4.place(x=c_x3,y=0)
    canvas_5.place(x=c_x4,y=0)
    if c_x != 0:
        main.after(10,SlideBackProfile)

def lemondas(fogl):
    for i in range(0,len(foglalasok)):
        if foglalasok[i] == fogl:
            foglalasok.pop(i)
            break

    with open("./verysecret/foglalas.txt", "r") as f:
        lines = f.readlines()
    with open("./verysecret/foglalas.txt", "w") as f:
        for line in lines:
            if line != f"{fogl.idopont.year}-{fogl.idopont.month}-{fogl.idopont.day};{fogl.szalloda.id};{fogl.szobaszam};{username.get()};\n":
                f.write(line)
    
    ctypes.windll.user32.MessageBoxW(0, f"Sikeresen lemondta az alábbi foglalását:\n{fogl.szalloda.nev}\n{fogl.szobaszam}\n{fogl.idopont.year}-{fogl.idopont.month}-{fogl.idopont.day}", "Siker!", 0)
    SlideBackProfile()

def getRegPage(event=None):
    global clx
    global crx
    clx -= 10
    crx -= 10
    canvas.place(x=clx,y=0)
    canvas_reg.place(x=crx,y=0)
    if crx != 0:
        main.after(10,getRegPage)
    
def getLogPage(event=None):
    global clx
    global crx
    clx += 10
    crx += 10
    canvas.place(x=clx,y=0)
    canvas_reg.place(x=crx,y=0)
    if clx != 0:
        main.after(10,getLogPage)

def register():
    if(reg_fel.get() != "" and reg_pass.get() != "" and reg_pass_again.get() != ""):
        if(reg_pass.get() == reg_pass_again.get()):
            egyedi = True
            for i in range(0,len(felhasznalok)):
                if felhasznalok[i].username == reg_fel.get():
                    egyedi = False
            if egyedi:
                f = open("./verysecret/felhasznalok.txt", "a")
                f.write(f"{reg_fel.get()};{reg_pass.get()};\n")
                f.close()
                felhasznalok.append(Felhasznalo(reg_fel.get(),reg_pass.get()))
                ctypes.windll.user32.MessageBoxW(0, "Sikeres regisztráció!", "Siker!", 0)
                getLogPage()
            else:
                ctypes.windll.user32.MessageBoxW(0, "Már létezik ilyen nevű felhasználó!", "Hiba!", 0)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Nem egyezik a jelszó!", "Hiba!", 0)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Töltse ki az összes mezőt!", "Hiba!", 0)


#region Szállodák képernyő
canvas_2 = tk.Canvas(main,bg="#2694E8",width=500,height=500)
canvas_2.place(x=0,y=0)
hotel_kiv = tk.Label(canvas_2,bg="#2694E8",text="Válasszon hotelt",font=('Segoe UI Black',24))
hotel_kiv.place(x=100,y=20,width=300,height=60)

image_p=Image.open('./pics/profpicround.jpg')
img_p=image_p.resize((60, 60))
my_img_p=ImageTk.PhotoImage(img_p)
user_btn = tk.Button(canvas_2, image=my_img_p, command=doProfilePage)
user_btn["bg"] = "#2694E8"
user_btn["activebackground"] = "#2694E8"
user_btn["border"] = "0"
user_btn.place(x=420,y=10,width=60,height=60)

user_name_lbl = tk.Label(canvas_2,bg="#2694E8",justify="center")
user_name_lbl.place(x=430,y=70)

image=Image.open('./pics/h1_round.png')
img=image.resize((207, 152))
my_img1=ImageTk.PhotoImage(img)
roundedbutton = tk.Button(canvas_2, image=my_img1, command=lambda: chosenHotel(0))
roundedbutton["bg"] = "#2694E8"
roundedbutton["activebackground"] = "#2694E8"
roundedbutton["border"] = "0"
roundedbutton.place(x=30,y=100, width=207,height=152)

hotel_1_name = tk.Label(canvas_2,text=szallodak[0].nev,font='Arial 12 bold',bg="#2694E8")
hotel_1_name.place(x=70,y=255)


image=Image.open('./pics/h2_round.png')
img=image.resize((207, 152))
my_img2=ImageTk.PhotoImage(img)
roundedbutton = tk.Button(canvas_2, image=my_img2, command=lambda: chosenHotel(1))
roundedbutton["bg"] = "#2694E8"
roundedbutton["activebackground"] = "#2694E8"
roundedbutton["border"] = "0"
roundedbutton.place(x=270,y=100, width=207,height=152)

hotel_1_name = tk.Label(canvas_2,text=szallodak[1].nev,font='Arial 12 bold',bg="#2694E8")
hotel_1_name.place(x=345,y=255)


image=Image.open('./pics/h3_round.png')
img=image.resize((207, 152))
my_img3=ImageTk.PhotoImage(img)
roundedbutton = tk.Button(canvas_2, image=my_img3, command=lambda: chosenHotel(2))
roundedbutton["bg"] = "#2694E8"
roundedbutton["activebackground"] = "#2694E8"
roundedbutton["border"] = "0"
roundedbutton.place(x=30,y=300, width=207,height=152)

hotel_1_name = tk.Label(canvas_2,text=szallodak[2].nev,font='Arial 12 bold',bg="#2694E8")
hotel_1_name.place(x=75,y=455)


image=Image.open('./pics/h4_round.png')
img=image.resize((207, 152))
my_img4=ImageTk.PhotoImage(img)
roundedbutton = tk.Button(canvas_2, image=my_img4, command=lambda: chosenHotel(3))
roundedbutton["bg"] = "#2694E8"
roundedbutton["activebackground"] = "#2694E8"
roundedbutton["border"] = "0"
roundedbutton.place(x=270,y=300, width=207,height=152)

hotel_1_name = tk.Label(canvas_2,text=szallodak[3].nev,font='Arial 12 bold',bg="#2694E8")
hotel_1_name.place(x=315,y=455)
#endregion

#region Kiválasztott hotel képernyő
c_x=0
c_x2=500

canvas_3 = tk.Canvas(main,bg="#2694E8",width=500,height=500)
canvas_3.place(x=500,y=0)

roundedbutton1 = tk.Button(canvas_3, command=lambda: chosenRoom(0))
roundedbutton1["bg"] = "#2694E8"
roundedbutton1["activebackground"] = "#2694E8"
roundedbutton1["border"] = "0"
roundedbutton1.place(x=30,y=50, width=207,height=152)

room_1_name = tk.Label(canvas_3,text="",font='Arial 12 bold',bg="#2694E8")
room_1_name.place(x=60,y=205)

roundedbutton2 = tk.Button(canvas_3, command=lambda: chosenRoom(1))
roundedbutton2["bg"] = "#2694E8"
roundedbutton2["activebackground"] = "#2694E8"
roundedbutton2["border"] = "0"
roundedbutton2.place(x=270,y=50, width=207,height=152)

room_2_name = tk.Label(canvas_3,text="",font='Arial 12 bold',bg="#2694E8")
room_2_name.place(x=300,y=205)

roundedbutton3 = tk.Button(canvas_3, command=lambda: chosenRoom(2))
roundedbutton3["bg"] = "#2694E8"
roundedbutton3["activebackground"] = "#2694E8"
roundedbutton3["border"] = "0"
roundedbutton3.place(x=30,y=250, width=207,height=152)

room_3_name = tk.Label(canvas_3,text="",font='Arial 12 bold',bg="#2694E8")
room_3_name.place(x=60,y=405)

roundedbutton4 = tk.Button(canvas_3, command=lambda: chosenRoom(3))
roundedbutton4["bg"] = "#2694E8"
roundedbutton4["activebackground"] = "#2694E8"
roundedbutton4["border"] = "0"
roundedbutton4.place(x=270,y=250, width=207,height=152)

room_4_name = tk.Label(canvas_3,text="",font='Arial 12 bold',bg="#2694E8")
room_4_name.place(x=300,y=405)

image_backbtn=Image.open(f'./pics/widget_bg/visszaBtn.png')
img_backbtn=image_backbtn.resize((175, 53))
my_img_backbtn=ImageTk.PhotoImage(img_backbtn)
back_btn = tk.Button(canvas_3,image=my_img_backbtn,command=slideToTheRight)
back_btn["bg"] = "#2694E8"
back_btn["activebackground"] = "#2694E8"
back_btn["border"] = "0"
back_btn.place(x=167,y=436)
#endregion

#region Kiválasztott szoba képernyő
c_x3 = 1000
canvas_4 = tk.Canvas(main,bg="#2694E8",width=500,height=500)
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

back_btn2 = tk.Button(canvas_4,text="Vissza",image=my_img_backbtn,command=slideRightRoom)
back_btn2["bg"] = "#2694E8"
back_btn2["activebackground"] = "#2694E8"
back_btn2["border"] = "0"
back_btn2.place(x=50,y=440)

image_foglbtn=Image.open(f'./pics/widget_bg/lefoglalasBtn.png')
img_foglbtn=image_foglbtn.resize((248, 66))
my_img_foglbtn=ImageTk.PhotoImage(img_foglbtn)
btn_fog = tk.Button(canvas_4,text="FOGLALÁS",image=my_img_foglbtn,command=dateSelectedVerifier)
btn_fog["bg"] = "#2694E8"
btn_fog["activebackground"] = "#2694E8"
btn_fog["border"] = "0"
btn_fog.place(x=240,y=420)

img = tk.Label(canvas_4)
img.place(x=28,y=20,width=245,height=184)
szobaszam = tk.Label(canvas_4,text="Szobaszám: 420",font="Ariel 13 bold",bg="#2694E8")
szobaszam.place(x=65,y=209,width=160,height=31)

ert_1 = tk.Label(canvas_4,text="Értékelés:",bg="#2694E8",font="Ariel 12 bold")
ert_2 = tk.Label(canvas_4,text="8.4",bg="#2694E8",font="Ariel 14 bold")
ert_3 = tk.Label(canvas_4,text="(1254 értékelés)",bg="#2694E8",font="Ariel 10 bold")
ert_1.place(x=337,y=10)
ert_2.place(x=357,y=30)
ert_3.place(x=325,y=54)

kul = tk.Label(canvas_4,text="Különlegességek:",bg="#2694E8",font="Ariel 12")
kul1 = tk.Label(canvas_4,text="• WC\n• Terasz\n• Kilátás\n• Hangszigetelt ablakok\n• Minibár",bg="#2694E8",font="Ariel 12 italic")
kul.place(x=320,y=85)
kul1.place(x=278,y=106,width=200,height=110)
#endregion

#region Saját fiók képernyő
c_x4 = -500
canvas_5 = tk.Canvas(main,bg="#2694E8",width=500,height=500)
canvas_5.place(x=-500,y=0)

canvas_foglist = tk.Canvas(canvas_5)

image=Image.open(f'./pics/profpicround.jpg')
img_prof=image.resize((80, 80))
my_img=ImageTk.PhotoImage(img_prof)
pic_label = tk.Label(canvas_5,image=my_img)
pic_label["bg"] = "#2694E8"
pic_label["activebackground"] = "#2694E8"
pic_label["border"] = "0"
pic_label.place(x=170,y=10,width=80,height=80)

label_nev = tk.Label(canvas_5,text="Tesztt",font="Ariel 22 bold",bg="#2694E8")
label_nev.place(x=260,y=35)

label_fogl = tk.Label(canvas_5,text="Foglalások:",font="Ariel 15 bold",bg="#2694E8")
label_fogl.place(x=30,y=110)

btn2 = tk.Button(canvas_5,text="Vissza",image=my_img_backbtn,command=SlideBackProfile)
btn2["bg"] = "#2694E8"
btn2["activebackground"] = "#2694E8"
btn2["border"] = "0"
btn2.place(x=170,y=420)

v = tk.Scrollbar(canvas_foglist)
v.pack(side = "right", fill = "y")
t = tk.Text(canvas_foglist, width = 30, height = 17, wrap = "none",
yscrollcommand = v.set,bg="#2694E8")
van_ilyen = False
t.tag_configure("center", justify='center')
t.tag_add("center", 1.0, "end")
t.config(state="disabled")
t.pack(side="top", fill="x")
v.config(command=t.yview)
canvas_foglist["bg"] = "#2694E8"
canvas_foglist.place(x=25,y=150,width=470,height=250)
#endregion

#region Belépő képernyő
block_y=0
clx = 0
canvas = tk.Canvas(main,bg="#2694E8",width=500,height=500)
canvas.place(x=0,y=0)

szf1_lbl = tk.Label(canvas,text="Szobafoglaló",font=('Segoe UI Black',44),bg="#2694E8",fg="white")
szf1_lbl.place(x=64,y=10)
reg1_lbl = tk.Label(canvas,text="Belépés",font=('Arial',22),bg="#2694E8",fg="white")
reg1_lbl.place(x=192,y=98)

image_btn=Image.open(f'./pics/widget_bg/entryblue.png')
img_btn=image_btn.resize((320, 56))
my_img_btn=ImageTk.PhotoImage(img_btn)

lbl11 = tk.Label(canvas,text="Felhasználónév:",fg="white",bg="#2694E8",font=('Ariel',14))
lbl11.place(x=104,y=183)
ent_bg1 = tk.Label(canvas,image=my_img_btn,bg="#2694E8")
ent_bg1.place(x=85,y=211,width=320,height=56)
username = tk.Entry(canvas,font=('Ariel',15),bg="#86BEE9",border=0)
username.place(x=105,y=215,width=250,height=40)

lbl21 = tk.Label(canvas,text="Jelszó:",fg="white",bg="#2694E8",font=('Ariel',14))
lbl21.place(x=104,y=263)
ent_bg21 = tk.Label(canvas,image=my_img_btn,bg="#2694E8")
ent_bg21.place(x=85,y=301,width=320,height=56)
password = tk.Entry(canvas,font=('Ariel',15),bg="#86BEE9",border=0,show="*")
password.place(x=105,y=305,width=250,height=40)

alr1 = tk.Label(canvas,text="Még nincs fiókod?",font=('Ariel',12),fg="white",bg="#2694E8")
alr1.place(x=143,y=400)
login_lbl1 = tk.Label(canvas,text="Regisztrálj",font=('Ariel',12),fg="#002979",bg="#2694E8")
login_lbl1.bind("<Button-1>",getRegPage)
login_lbl1.place(x=275,y=400)

image21=Image.open(f'./pics/widget_bg/belepesBtn.png')
img21=image21.resize((175, 53))
my_img21=ImageTk.PhotoImage(img21)
reg_btn1 = tk.Button(canvas,image=my_img21,command=login)
reg_btn1["bg"] = "#2694E8"
reg_btn1["activebackground"] = "#2694E8"
reg_btn1["border"] = "0"
reg_btn1.place(x=167,y=436)
#endregion

#region Regisztrálás képernyő
crx = 500
canvas_reg = tk.Canvas(main,bg="#2694E8",width=500,height=500)
canvas_reg.place(x=500,y=0)

szf_lbl = tk.Label(canvas_reg,text="Szobafoglaló",font=('Segoe UI Black',44),bg="#2694E8",fg="white")
szf_lbl.place(x=64,y=10)
reg_lbl = tk.Label(canvas_reg,text="Regisztráció",font=('Arial',22),bg="#2694E8",fg="white")
reg_lbl.place(x=162,y=98)

lbl1 = tk.Label(canvas_reg,text="Felhasználónév:",fg="white",bg="#2694E8",font=('Ariel',14))
lbl1.place(x=104,y=153)
ent_bg = tk.Label(canvas_reg,image=my_img_btn,bg="#2694E8")
ent_bg.place(x=85,y=181,width=320,height=56)
reg_fel = tk.Entry(canvas_reg,font=('Ariel',15),bg="#86BEE9",border=0)
reg_fel.place(x=105,y=185,width=250,height=40)

lbl2 = tk.Label(canvas_reg,text="Jelszó:",fg="white",bg="#2694E8",font=('Ariel',14))
lbl2.place(x=104,y=233)
ent_bg2 = tk.Label(canvas_reg,image=my_img_btn,bg="#2694E8")
ent_bg2.place(x=85,y=261,width=320,height=56)
reg_pass = tk.Entry(canvas_reg,font=('Ariel',15),bg="#86BEE9",border=0,show="*")
reg_pass.place(x=105,y=265,width=250,height=40)

lbl3 = tk.Label(canvas_reg,text="Jelszó ismét:",fg="white",bg="#2694E8",font=('Ariel',14))
lbl3.place(x=104,y=313)
ent_bg3 = tk.Label(canvas_reg,image=my_img_btn,bg="#2694E8")
ent_bg3.place(x=85,y=341,width=320,height=56)
reg_pass_again = tk.Entry(canvas_reg,font=('Ariel',15),bg="#86BEE9",border=0,show="*")
reg_pass_again.place(x=105,y=345,width=250,height=40)

alr = tk.Label(canvas_reg,text="Már van fiókod?",font=('Ariel',12),fg="white",bg="#2694E8")
alr.place(x=148,y=400)
login_lbl = tk.Label(canvas_reg,text="Jelentkezz be",font=('Ariel',12),fg="#002979",bg="#2694E8")
login_lbl.bind("<Button-1>",getLogPage)
login_lbl.place(x=265,y=400)

image_reg=Image.open(f'./pics/widget_bg/registerBtn.png')
img_reg=image_reg.resize((175, 53))
my_img_reg=ImageTk.PhotoImage(img_reg)
reg_btn = tk.Button(canvas_reg,image=my_img_reg,command=register)
reg_btn["bg"] = "#2694E8"
reg_btn["activebackground"] = "#2694E8"
reg_btn["border"] = "0"
reg_btn.place(x=167,y=436)
#endregion

main.mainloop()