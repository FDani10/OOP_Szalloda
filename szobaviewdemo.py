import tkinter as tk
import tkintermapview
from tkcalendar import Calendar
import datetime

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

def dateSelectedVerifier():
    date = cal.get_date().split('/')
    caldate = datetime.datetime(int(date[2])+2000,int(date[0]),int(date[1]))
    if to_integer(caldate) > to_integer(datetime.datetime.now()):
        print("Very nice. Great success")
    else:
        print("Idióta")

main = tk.Tk()

main.geometry("500x500")
main.configure(background="#8abee6")

label = tk.LabelFrame(main)
label.place(x=31,y=240,width=190,height=190)

map = tkintermapview.TkinterMapView(label,width=190,height=190)
map.set_position(47.3809,19.2157,marker=True)
map.set_zoom(15)
map.place(x=0,y=0)

class MyCalendar(Calendar):
    def __init__(self, master=None, **kw):
        self._disabled_dates = []
        Calendar.__init__(self, master, **kw)

    def disable_date(self, date):
        self._disabled_dates.append(date)
        mi, mj = self._get_day_coords(date)
        if mi is not None:  # date is displayed
            self._calendar[mi][mj].state(['disabled'])

    def _display_calendar(self):
        Calendar._display_calendar(self)
        for date in self._disabled_dates:
            mi, mj = self._get_day_coords(date)
            if mi is not None:  # date is displayed
                self._calendar[mi][mj].state(['disabled'])

cal = MyCalendar(main, selectmode='day',
                 year=2024, month=4, disableddaybackground="gray",
                 day=19)
cal.disable_date(datetime.date(2024, 4, 21))
cal.disable_date(datetime.date(2024, 4, 25))
cal.disable_date(datetime.date(2024, 4, 30))
cal.place(x=240,y=224)

btn = tk.Button(main,text="FOGLALÁS",command=dateSelectedVerifier)
btn.place(x=240,y=414,width=250,height=66)

btn2 = tk.Button(main,text="Vissza",command=dateSelectedVerifier)
btn2.place(x=60,y=440,width=135,height=40)

from PIL import Image, ImageTk

image=Image.open(f'./pics/rooms/room2.jpg')
img=image.resize((245, 184))
my_img=ImageTk.PhotoImage(img)

img = tk.Label(main,image=my_img)
img.place(x=28,y=20,width=245,height=184)
szobaszam = tk.Label(main,text="Szobaszám: 420",font="Ariel 15 bold",bg="#8abee6")
szobaszam.place(x=75,y=209,width=160,height=31)

ert_1 = tk.Label(main,text="Értékelés:",bg="#8abee6",font="Ariel 12 bold")
ert_2 = tk.Label(main,text="8.4",bg="#8abee6",font="Ariel 14 bold")
ert_3 = tk.Label(main,text="(1254 értékelés)",bg="#8abee6",font="Ariel 10 bold")
ert_1.place(x=337,y=10)
ert_2.place(x=357,y=30)
ert_3.place(x=325,y=54)

kul = tk.Label(main,text="Különlegességek:",bg="#8abee6",font="Ariel 12")
kul1 = tk.Label(main,text="• WC\n• Terasz\n• Kilátás\n• Hangszigetelt ablakok\n• Minibár",bg="#8abee6",font="Ariel 12 italic")
kul.place(x=320,y=85)
kul1.place(x=293,y=110)

main.mainloop()