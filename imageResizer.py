#Nem akartam a main.py-be tenni, ezért külön fájlt csináltam neki

from PIL import Image, ImageTk

def picSizer():
    pics = []
    for i in range(1,17):
        image=Image.open(f'./pics/rooms/room{i}.jpg')
        img=image.resize((207, 152))
        my_img=ImageTk.PhotoImage(img)
        pics.append(my_img)
    return pics