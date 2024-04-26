import tkinter as tk
from PIL import Image,ImageTk

main = tk.Tk()

main.geometry("500x500")
main.configure(background="#8abee6")

canvas = tk.Canvas(main)

image=Image.open(f'./pics/profpicround.jpg')
img=image.resize((100, 100))
my_img=ImageTk.PhotoImage(img)
pic_label = tk.Label(main,image=my_img)
pic_label["bg"] = "#8abee6"
pic_label["activebackground"] = "#8abee6"
pic_label["border"] = "0"
pic_label.place(x=70,y=30,width=100,height=100)
  
v = tk.Scrollbar(canvas)
  
v.pack(side = "right", fill = "y")
          
t = tk.Text(canvas, width = 30, height = 17, wrap = "none",
         yscrollcommand = v.set,bg="#8abee6")
  
t.tag_configure("center", justify='center')
foglalas_txt = open("./verysecret/foglalas.txt", "r")
foglalas_txt.readline()

szalloda_nev = ["Generus Hotel","Stacio","One Star Motel","Margaret Hotel"]

for line in foglalas_txt:
    btn_text = tk.Button(t,text="Lemondás",command=lambda:print("lemondva"))
    sorok = line.split(';')
    t.insert("end",f"{szalloda_nev[int(sorok[1])-1]} | {sorok[2]} | {sorok[0]} | 19 500Ft | ")
    t.window_create("end", window=btn_text)
    t.insert("end", "\n")
    t.insert("end","\n")
  
  
t.tag_add("center", 1.0, "end")
t.config(state="disabled")
t.pack(side="top", fill="x")
  
  
v.config(command=t.yview)

canvas["bg"] = "#8abee6"
canvas.place(x=25,y=150,width=470,height=250)

btn2 = tk.Button(main,text="Vissza",command=lambda:print("hello"))
btn2.place(x=190,y=440,width=120,height=40)

main.mainloop()