from tkinter import *
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("Tkinter.db")


pencere = Tk()
pencere.title("Giriş Yap")
pencere.configure(bg="#F9F6F2")
pencere.geometry("450x250")
pencere.resizable(width=False,height=False)
pencere.option_add("*Font", "Helvetica 12")

kAd = Label(pencere,text="Kullanıcı Adı")
kAd.place(relx=0.41,rely=0.1)

E1 = Entry(pencere,width=22)
E1.place(relx=0.32,rely=0.2)

parola = Label(pencere,text="Parola")
parola.place(relx=0.44,rely=0.3)

E2 = Entry(pencere, show="*" ,  width=25)
E2.place(relx=0.32,rely=0.4,relwidth=0.4)

def goster():
    if c1_value.get():
        E2.config(show="")
        L0.config(text="Gizle")
    else:
        E2.config(show="*")
        L0.config(text="Göster")

c1_value = BooleanVar()
c1_value.set(FALSE)
C1 = Checkbutton(pencere,variable=c1_value,command=goster)  
C1.place(relx=0.73,rely=0.4)
L0 = Label(pencere,text="Göster")
L0.place(relx=0.79,rely=0.4)   

def giris():
        cursor = connection.execute("""select UserName,Password from User""")
        giris_=False
        for row in cursor:
            if row[0]==str(E1.get()) and row[1]==str(E2.get()):
                giris_ = True
        if giris_ :
            messagebox.showinfo("Giriş Başarılı","Hoşgeldiniz")
            E1.delete("0","end")
            E2.delete("0","end")
            pencere.destroy()
        else:
            E1.delete("0","end")
            E2.delete("0","end")
            messagebox.showwarning("Giriş Başarısız","Kullanıcı Bulunamadı")
                

b1 = Button(pencere,text="Giriş", fg="white", bg="#2185C5", activebackground="#1E6FA6",command=giris)
b1.place(relx=0.43,rely=0.55,relheight=0.11,relwidth=0.15)

L1 = Label(pencere,text = "Hesabınız yok mu?")
L2 = Label(pencere,text="Hemen Bir Tane Oluşturun")
L1.place(relx=0.3,rely=0.7)
L2.place(relx=0.3,rely=0.77)

def kayit():
    yeni_pencere = Toplevel(pencere)
    yeni_pencere.title("Kayıt Ol")
    

b2 = Button(pencere,text="Kayıt Ol", fg="white", bg="#2185C5", activebackground="#1E6FA6",command=kayit)
b2.place(relx = 0.3, rely=0.87,relheight=0.11,relwidth=0.15)


pencere.mainloop()
