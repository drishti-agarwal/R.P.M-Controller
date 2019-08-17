
from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry('600x600')
root.config(bg='light green')

rpm=1000
Label(root,text='R.P.M METER',fg='white',bg='purple',bd=10,
      font=('arial',30,'bold'),relief=RAISED).place(x=550,y=0)
l1=Label(root,text=rpm,fg='white',bg='orange',
         bd=10,font=('arial',20,'bold'),relief=RAISED)
l1.place(x=650,y=100)
def v():
        global rpm
        rpm=1000

def acclerate():
        global rpm
        rpm+=500
        l1.config(text=rpm)
        try:
            if rpm>3000:

                import winsound
                winsound.Beep(3000,1000)
                messagebox.showinfo(title='ALERT!!!', message='too high')

        except:
            # rpm-=2000
            # l1.config(text=rpm)
            messagebox.showinfo(title='ALERT!!!', message='use break')
        return rpm
print(acclerate())
def reduce():
        global rpm
        rpm-=500
        l1.config(text=rpm)
        try:
            if rpm<1000:
                messagebox.showinfo(title='ALERT!!!', message='too low')
                import winsound
                winsound.Beep(3000,1000)
        except:
                messagebox.showinfo(title='ALERT!!!', message='use acclerate')




Button(root,text='ACCELERATOR',fg='white',bg='red',bd=10,
       font=('arial',20,'bold'),command=acclerate).place(x=450,y=200)
Button(root,text='BREAK',fg='white',bg='red',bd=10,
       font=('arial',20,'bold'),command=reduce).place(x=750,y=200)
root.mainloop()

# def change_label():
#     x='This is changed'
#     l1.config(text=x,bg='brown',font=40)