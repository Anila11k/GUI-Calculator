import tkinter 
from tkinter import *


window=Tk()
window.title("CALCULATOR")
window.geometry("500x600")
window.configure(bg="gray")

equation=""
def show(value):
    global equation
    equation+=value
    lab_result.config(text=equation)

def clear():
    global equation
    equation=""
    lab_result.config(text=equation)

def calculate():
    global equation
    result= ""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    lab_result.config(text=result)


lab_result=Label(window,fg="white",bg="black",width=32,height=2,font=("arial",18))
lab_result.place(x=15,y=10)
 
b1=Button(window,text="7",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("7"))
b1.place(x=15,y=180)


b2=Button(window,text="8",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("8"))
b2.place(x=130,y=180)


b3=Button(window,text="9",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("9"))
b3.place(x=245,y=180)

b18=Button(window,text="*",width=5,height=1,font=("arial",25),bg=("light blue"),command=lambda:show("*"))
b18.place(x=370,y=180)

b4=Button(window,text="4",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("4"))
b4.place(x=15,y=270)

b5=Button(window,text="5",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("5"))
b5.place(x=130,y=270)

b6=Button(window,text="6",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("6"))
b6.place(x=250,y=270)

b6=Button(window,text="-",width=5,height=1,font=("arial",25),bg=("light blue"),command=lambda:show("-"))
b6.place(x=370,y=270)


b7=Button(window,text="1",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("1"))
b7.place(x=15,y=360)

b8=Button(window,text="2",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("2"))
b8.place(x=130,y=360)

b9=Button(window,text="3",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("3"))
b9.place(x=250,y=360)

b9=Button(window,text="+",width=5,height=1,font=("arial",25),bg=("light blue"),command=lambda:show("+"))
b9.place(x=370,y=360)

b10=Button(window,text="00",width=5,height=1,font=("arial",25),bg=("light blue"),command=lambda:show("00"))
b10.place(x=15,y=450)


b11=Button(window,text="0",width=5,height=1,font=("arial",25),bg=("light blue"),command=lambda:show("0"))
b11.place(x=130,y=450)


b12=Button(window,text=".",width=5,height=1,font=("arial",25),bg=("light blue"),command=lambda:show("."))
b12.place(x=250,y=450)


b13=Button(window,text="=",width=5,height=1,font=("arial",25),bg=("orange"),command=calculate)
b13.place(x=370,y=450)

b14=Button(window,text="AC",width=5,height=1,font=("arial",25),bg=("light green"),command=lambda:clear())
b14.place(x=15,y=90)

b15=Button(window,text="%",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:show("%"))
b15.place(x=130,y=90)

b16=Button(window,text="c",width=5,height=1,font=("arial",25),bg=("black"),fg=("white"),command=lambda:clear())
b16.place(x=250,y=90)



b17=Button(window,text="/",width=5,height=1,font=("arial",25),bg=("light blue"),command=lambda:show("/"))
b17.place(x=370,y=90)
window.mainloop()








window.mainloop()

