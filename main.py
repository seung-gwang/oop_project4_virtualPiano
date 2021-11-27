from tkinter import*
import time
import datetime
import pygame

pygame.init()

root=Tk()

root.title('Virtual Piano')
root.geometry('1600x800+0+0')
root.configure(background='white')

ABC = Frame(root, bg="powder blue", bd=20, relief =RIDGE)
ABC.grid()

ABC1 = Frame(ABC, bg="powder blue", bd=20, relief =RIDGE)
ABC1.grid()

ABC2 = Frame(ABC, bg="powder blue", bd=20, relief =RIDGE)
ABC2.grid()

ABC3 = Frame(ABC, bg="powder blue", bd=20, relief =RIDGE)
ABC3.grid()

str1 = StringVar()
str1.set("Team 3")

Date1=StringVar() #날짜와 시계를 넣어주었는데 굳이 필요없을듯. 대신 스톱워치를 넣어주는게 더 좋을 것 같음
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

#==================흑건 사운드====================
def value_Cs():
    str1.set("C#")
    sound=pygame.mixer.Sound("C:\music_piano\C_s.wav")
    sound.play()

def value_Ds():
    str1.set("D#")
    sound=pygame.mixer.Sound("C:\music_piano\D_s.wav")
    sound.play()

def value_Fs():
    str1.set("F#")
    sound=pygame.mixer.Sound("C:\music_piano\F_s.wav")
    sound.play()

def value_Gs():
    str1.set("G#")
    sound=pygame.mixer.Sound("C:\music_piano\G_s.wav")
    sound.play()

def value_As():
    str1.set("A#")
    sound=pygame.mixer.Sound("C:\music_piano\Bb.wav")
    sound.play()

def value_Cs1():
    str1.set("C#1")
    sound=pygame.mixer.Sound("C:\music_piano\C_s1.wav")
    sound.play()

def value_Ds1():
    str1.set("D#1")
    sound=pygame.mixer.Sound("C:\music_piano\D_s1.wav")
    sound.play()

#==================백건 사운드====================

def value_C():
    str1.set("C")
    sound=pygame.mixer.Sound("C:\music_piano\C.wav")
    sound.play()

def value_D():
    str1.set("D")
    sound=pygame.mixer.Sound("C:\music_piano\D.wav")
    sound.play()

def value_E():
    str1.set("E")
    sound=pygame.mixer.Sound("C:\music_piano\E.wav")
    sound.play()

def value_F():
    str1.set("F")
    sound=pygame.mixer.Sound("C:\music_piano\F.wav")
    sound.play()

def value_G():
    str1.set("G")
    sound=pygame.mixer.Sound("C:\music_piano\G.wav")
    sound.play()

def value_A():
    str1.set("A")
    sound=pygame.mixer.Sound("C:\music_piano\A.wav")
    sound.play()

def value_B():
    str1.set("B")
    sound=pygame.mixer.Sound("C:\music_piano\B.wav")
    sound.play()

def value_C1():
    str1.set("C")
    sound=pygame.mixer.Sound("C:\music_piano\C1.wav")
    sound.play()

def value_D1():
    str1.set("D1")
    sound=pygame.mixer.Sound("C:\music_piano\D1.wav")
    sound.play()

def value_E1():
    str1.set("E1")
    sound=pygame.mixer.Sound("C:\music_piano\E1.wav")
    sound.play()

def value_F1():
    str1.set("F1")
    sound=pygame.mixer.Sound("C:\music_piano\F1.wav")
    sound.play()

#===================라벨 디자인========================

Label(ABC1, text="Virtual Piano",
font=('arial',25,'bold'),padx=8,pady=8, bd=4,bg="blue",
fg="white", justify=CENTER).grid(row=0,column=0,columnspan=11)

#===================날짜와 시간========================

txtDate=Entry(ABC1, textvariable=Date1, font=('arial',18,'bold'),bd=34,bg="blue",
fg="white", width=28, justify=CENTER).grid(row=1,column=0,pady=1)

txtDisplay=Entry(ABC1, textvariable=str1, font=('arial',18,'bold'),bd=34,bg="blue",
fg="white", width=28, justify=CENTER).grid(row=1,column=1,pady=1)

txtTime=Entry(ABC1, textvariable=Time1, font=('arial',18,'bold'),bd=34,bg="blue",
fg="white", width=28, justify=CENTER).grid(row=1,column=2,pady=1)

#===================흑건========================

btnSpace0=Button(ABC2, state=DISABLED, width=10,height=6, bg="powder blue", relief=FLAT)
btnSpace0.grid( row=0, column=0, padx=0,pady=0)

btnCs=Button(ABC2, height=6,width=6,bd=4,text="C#\nDb",bg="black",fg="white",font=('arial',18,'bold'),command=value_Cs)
btnCs.grid(row=0,column=1,padx=5,pady=5)

btnDs=Button(ABC2, height=6,width=6,bd=4,text="D#\nEb",bg="black",fg="white",font=('arial',18,'bold'),command=value_Ds)
btnDs.grid(row=0,column=2,padx=5,pady=5)

btnSpace2=Button(ABC2, state=DISABLED, width=15,height=6, bg="powder blue", relief=FLAT)
btnSpace2.grid( row=0, column=3, padx=0,pady=0)

btnFs=Button(ABC2, height=6,width=6,bd=4,text="F#\nGb", font=('arial',18,'bold'),command=value_Fs,bg="black",fg="white")
btnFs.grid(row=0,column=4,padx=5,pady=5)

btnGs=Button(ABC2, height=6,width=6,bd=4,text="G#\nAb", font=('arial',18,'bold'),command=value_Gs,bg="black",fg="white")
btnGs.grid(row=0,column=6, padx=5,pady=5)

btnAs=Button(ABC2, height=6,width=6,bd=4,text="A#\nBb", font=('arial',18,'bold'),command=value_As,bg="black",fg="white")
btnAs.grid(row=0,column=8, padx=5,pady=5)

btnSpace5=Button(ABC2, state=DISABLED, width=15,height=6, bg="powder blue", relief=FLAT)
btnSpace5.grid( row=0, column=9, padx=0,pady=0)

btnCs1=Button(ABC2, height=6,width=6,bd=4,text="C#1",bg="black",fg="white",font=('arial',18,'bold'),command=value_Cs1)
btnCs1.grid(row=0,column=10,padx=5,pady=5)

btnDs1=Button(ABC2, height=6,width=6,bd=4,text="D#1",bg="black",fg="white",font=('arial',18,'bold'),command=value_Ds1)
btnDs1.grid(row=0,column=12,padx=5,pady=5)

btnSpace7=Button(ABC2, state=DISABLED, width=30,height=6, bg="powder blue", relief=FLAT)
btnSpace7.grid( row=0, column=14, padx=0,pady=0)

#===================백건========================

btnC=Button(ABC3, height=8,width=6,bd=4,text="C", font=('arial',18,'bold'),command=value_C, bg="white",fg="black")
btnC.grid(row=0,column=0,padx=5,pady=5)

btnD=Button(ABC3, height=8,width=6,bd=4,text="D", font=('arial',18,'bold'),command=value_D, bg="white",fg="black")
btnD.grid(row=0,column=1,padx=5,pady=5)

btnE=Button(ABC3, height=8,width=6,bd=4,text="E", font=('arial',18,'bold'),command=value_E, bg="white",fg="black")
btnE.grid(row=0,column=2,padx=5,pady=5)

btnF=Button(ABC3, height=8,width=6,bd=4,text="F", font=('arial',18,'bold'),command=value_F, bg="white",fg="black")
btnF.grid(row=0,column=3,padx=5,pady=5)

btnG=Button(ABC3, height=8,width=6,bd=4,text="G", font=('arial',18,'bold'),command=value_G, bg="white",fg="black")
btnG.grid(row=0,column=4,padx=5,pady=5)

btnA=Button(ABC3, height=8,width=6,bd=4,text="A", font=('arial',18,'bold'),command=value_A, bg="white",fg="black")
btnA.grid(row=0,column=5,padx=5,pady=5)

btnB=Button(ABC3, height=8,width=6,bd=4,text="B", font=('arial',18,'bold'),command=value_B, bg="white",fg="black")
btnB.grid(row=0,column=6,padx=5,pady=5)

btnC1=Button(ABC3, height=8,width=6,bd=4,text="C1", font=('arial',18,'bold'),command=value_C1, bg="white",fg="black")
btnC1.grid(row=0,column=7,padx=5,pady=5)

btnD1=Button(ABC3, height=8,width=6,bd=4,text="D1", font=('arial',18,'bold'),command=value_D1, bg="white",fg="black")
btnD1.grid(row=0,column=8,padx=5,pady=5)

btnE1=Button(ABC3, height=8,width=6,bd=4,text="E1", font=('arial',18,'bold'),command=value_E1, bg="white",fg="black")
btnE1.grid(row=0,column=9,padx=5,pady=5)

btnF1=Button(ABC3, height=8,width=6,bd=4,text="F1", font=('arial',18,'bold'),command=value_F1, bg="white",fg="black")
btnF1.grid(row=0,column=10,padx=5,pady=5)

root.mainloop()