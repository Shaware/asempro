from tkinter import *
from yt_dlp import YoutubeDL

def h_quality():
    try:
        url =entry.get()


        dec={
            'fromat':'best',
            'outtmpl':'downloads%(titles)s.%(ext)s'
        }
        with YoutubeDL(dec) as ydl:
            ydl.download([url])
            print("The vedio has downloaded")


    except Exception as ex:
        print("ERROR")   


def l_quality():
    try:
        url =entry.get()


        dec={
            'fromat':'wrost',
            'outtmpl':'downloads%(titles)s.%(ext)s'
        }
        with YoutubeDL(dec) as ydl:
            ydl.download([url])
            print("The vedio has downloaded")


    except Exception as ex:
        print("ERROR")

def audioo():
    try:
        url =entry.get()


        dec={
            'fromat':'bestaudio',
            'outtmpl':'downloads%(titles)s.%(ext)s'
        }
        with YoutubeDL(dec) as ydl:
            ydl.download([url])
            print("The vedio has downloaded")


    except Exception as ex:
        print("ERROR")





window =Tk()
window.title ("youtube")
window.geometry("600x400")
window.configure(bg="#CDB78E")

lable=Label (window,text ="Add your link here",bg=window['bg'])
lable.place(x=25,y=35)

entry=Entry(window,width=50)
entry.place (x=200,y=30)

pt_high=Button(window,text="High quality",command=h_quality)
pt_high.place (x=150,y=200)

pt_low=Button(window,text="Low quality",command=l_quality)
pt_low.place (x=250,y=200)

pt_audio=Button(window,text="git audio",command=audioo)
pt_audio.place (x=360,y=200)







window.mainloop()