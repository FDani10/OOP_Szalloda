import tkinter as tk

main = tk.Tk()

main.geometry("500x500")
main.configure(background="#8abee6")

btn2 = tk.Button(main,text="Vissza",command=lambda:print("hello"))
btn2.place(x=190,y=440,width=120,height=40)

main.mainloop()