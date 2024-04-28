import tkinter as tk
from PIL import Image,ImageTk

main = tk.Tk()

main.geometry("500x500")

szallodak = ["One Star Motel","Stacio","Generus Hotel","Margaret Hotel"]

image=Image.open(f'./pics/rooms/room1.png')
img=image.resize((207, 152))
my_img=ImageTk.PhotoImage(img)


canvas_3 = tk.Canvas(main,bg="#2694E8",width=500,height=500)
canvas_3.place(x=0,y=0)
roundedbutton1 = tk.Button(canvas_3, command=lambda: print("teszt"),image=my_img)
roundedbutton1["bg"] = "#2694E8"
roundedbutton1["activebackground"] = "#2694E8"
roundedbutton1["border"] = "0"
roundedbutton1.place(x=30,y=50, width=207,height=152)

room_1_name = tk.Label(canvas_3,text="Szobaszám: 420",font='Arial 12 bold',bg="#2694E8")
room_1_name.place(x=60,y=205)

roundedbutton2 = tk.Button(canvas_3, command=lambda: print("teszt"),image=my_img)
roundedbutton2["bg"] = "#2694E8"
roundedbutton2["activebackground"] = "#2694E8"
roundedbutton2["border"] = "0"
roundedbutton2.place(x=270,y=50, width=207,height=152)

room_2_name = tk.Label(canvas_3,text="Szobaszám: 420",font='Arial 12 bold',bg="#2694E8")
room_2_name.place(x=300,y=205)

roundedbutton3 = tk.Button(canvas_3, command=lambda: print("teszt"),image=my_img)
roundedbutton3["bg"] = "#2694E8"
roundedbutton3["activebackground"] = "#2694E8"
roundedbutton3["border"] = "0"
roundedbutton3.place(x=30,y=250, width=207,height=152)

room_3_name = tk.Label(canvas_3,text="Szobaszám: 420",font='Arial 12 bold',bg="#2694E8")
room_3_name.place(x=60,y=405)

roundedbutton4 = tk.Button(canvas_3, command=lambda: print("teszt"),image=my_img)
roundedbutton4["bg"] = "#2694E8"
roundedbutton4["activebackground"] = "#2694E8"
roundedbutton4["border"] = "0"
roundedbutton4.place(x=270,y=250, width=207,height=152)

room_4_name = tk.Label(canvas_3,text="Szobaszám: 420",font='Arial 12 bold',bg="#2694E8")
room_4_name.place(x=300,y=405)

image_reg=Image.open(f'./pics/widget_bg/visszaBtn.png')
img_reg=image_reg.resize((175, 53))
my_img_reg=ImageTk.PhotoImage(img_reg)
reg_btn = tk.Button(canvas_3,image=my_img_reg,command=lambda:print("Hello back"))
reg_btn["bg"] = "#2694E8"
reg_btn["activebackground"] = "#2694E8"
reg_btn["border"] = "0"
reg_btn.place(x=167,y=436)
main.mainloop()