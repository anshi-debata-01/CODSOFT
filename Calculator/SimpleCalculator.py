from tkinter import *
root = Tk()
root.geometry("570x600")
root.title("Simple Calculator")
root.resizable(False,False)
root.configure(bg="#17161b")
equation = " "
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
def clear():
    global equation
    equation =" "
    label_result.config(text=equation)
def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

label_result = Label(width=54 , height =2 ,text = " ",font = ("calibri",30))
label_result.pack()

Button( text = "C" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "blue",command=lambda: clear()).place(x=10,y=107)
Button( text = "/" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("/")).place(x=150,y=107)
Button( text = "%" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("%")).place(x=290,y=107)
Button( text = "*" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("*")).place(x=430,y=107)

Button( text = "7" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("7")).place(x=10,y=200)
Button( text = "8" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("8")).place(x=150,y=200)
Button( text = "9" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("9")).place(x=290,y=200)
Button( text = "-" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("-")).place(x=430,y=200)

Button( text = "4" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("4")).place(x=10,y=300)
Button( text = "5" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("5")).place(x=150,y=300)
Button( text = "6" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("6")).place(x=290,y=300)
Button( text = "+" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("+")).place(x=430,y=300)

Button( text = "1" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("1")).place(x=10,y=400)
Button( text = "2" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("2")).place(x=150,y=400)
Button( text = "3" , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("3")).place(x=290,y=400)
Button( text = "0" , width =13 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show("0")).place(x=10,y=500)

Button( text = "." , width =5 , height =1 , font = ("calibri",30) , bd=1 , fg="white" , bg = "grey",command=lambda: show(".")).place(x=290,y=500)
Button( text = "=" , width =5 , height =3 , font = ("calibri",30) , bd=1 , fg="white" , bg = "orange",command=lambda: calculate()).place(x=430,y=400)


root.mainloop()