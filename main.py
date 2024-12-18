from tkinter import *
import tkinter.messagebox

window = Tk()
def click(number):
    num_entry.insert(100, number)
def reset():
    num_entry.delete(0,END)
def equal():

    #curent = num_entry.get()
    #list = curent.split("+")
    #total = float(list[0]) + float(list[0])
    #num_entry.delete(0, END)
    #num_entry.insert(0, total)

    try:
        result = str(eval(num_entry.get()))
        num_entry.delete(0, END)
        num_entry.insert(0, result)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error try again")

#----- screen --------

window.title("Simple Calculator")
window.geometry("500x500")
window.resizable(0,0)
window.config(padx=20, pady=20, bg="#9E9E9E")
num_entry = Entry(window, bd= 8, width=30, font="Arial 21", bg="lightblue")
num_entry.pack()
num_entry.focus()
#-----Button--------
btn0 = Button(window, text="0", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(0))
btn0.place(x=10,y=60)
btn1 = Button(window, text="1", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(1))
btn1.place(x=95,y=60)
btn2 = Button(window, text="2", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(2))
btn2.place(x=180,y=60)
btn3 = Button(window, text="3", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(3))
btn3.place(x=265,y=60)
btn4 = Button(window, text="4", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(4))
btn4.place(x=10,y=160)
btn5 = Button(window, text="5", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(5))
btn5.place(x=95, y=160)
btn6 = Button(window, text="6", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(6))
btn6.place(x=180,y=160)
btn7 = Button(window, text="7", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(7))
btn7.place(x=265,y=160)
btn8 = Button(window, text="8", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(8))
btn8.place(x=10,y=260)
btn9 = Button(window, text="9", bg="#A3E4D7", bd=9, padx=15, pady=15, font=("Ariel",20,"bold"), command=lambda: click(9))
btn9.place(x=95,y=260)

btn_note = Button(window, text=".", bg="#ff8000", bd=9, padx=18, pady=15, font=("Ariel",20,"bold"), command=lambda: click("."))
btn_note.place(x=180,y=260)
btn_reset = Button(window, text="C", bg="red", bd=9, padx=15, pady=14, font=("Ariel",20,"bold"), command=reset)
btn_reset.place(x=265,y=260)

#egal_image = PhotoImage(file="images/add.png")

egal_button = Button(window, text="=", bd=9, width=17, bg="#ABEBC6",padx=15, pady=15, font=("Ariel",20,"bold"), command=equal)
egal_button.place(x=10,y=360)
add_button = Button(window, text="+", bg="#01579B", bd=9, padx=18, pady=17, font=("Ariel",20,"bold"), command=lambda: click('+'))
add_button.place(x=350,y=60)
sub_button = Button(window, text="-", bg="#6D4C41", bd=9, padx=21, pady=15, command=lambda: click('-'), font=("Ariel",20,"bold"))
sub_button.place(x=350,y=160)
multi_button = Button(window, text="*", bg="#0080ff", bd=9, padx=20, pady=15, font=("Ariel",20,"bold"),command=lambda:click('*'))
multi_button.place(x=350,y=260)
div_button = Button(window, text="/", bg="#EDBB99", bd=9, padx=21, pady=15, font=("Ariel",20,"bold"),command=lambda:click('/'))
div_button.place(x=350,y=360)
window.mainloop()