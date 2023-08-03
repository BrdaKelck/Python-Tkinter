from tkinter import *
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect("Tkinter.db")


pencere = Tk()
pencere.geometry("450x250")
pencere.resizable(width=False, height=False)
pencere.title("Kayıt Ol")

# Arka plan rengi ve font stilini güncelleyelim
pencere.configure(bg="#F9F6F2")
pencere.option_add("*Font", "Helvetica 12")

L1 = Label(pencere, text="Email(*)", bg="#F9F6F2")
L1.place(relx=0.41, rely=0.1)

L2 = Label(pencere, text="Parola(*)", bg="#F9F6F2")
L2.place(relx=0.41, rely=0.3)

E1 = Entry(pencere, width=20, bg="white", fg="black")
E1.place(relx=0.3, rely=0.2)

E2 = Entry(pencere, show="*", width=20, bg="white", fg="black")
E2.place(relx=0.3, rely=0.4)

C1_variable = BooleanVar()
C1_variable.set(False)

L4 = Label(pencere, text="En az 6 harf", bg="#F9F6F2")
L4.place(relx=0.1, rely=0.4)

def goster():
    if C1_variable.get():
        E2.config(show="")
        L3.config(text="Gizle")
    else:
        E2.config(show="*")
        L3.config(text="Göster")

C1 = Checkbutton(pencere, variable=C1_variable, command=goster, bg="#F9F6F2")
C1.place(relx=0.6, rely=0.39)

L3 = Label(pencere, text="Göster", bg="#F9F6F2")
L3.place(relx=0.66, rely=0.39)

def kayitOl():
    if E1.get() and E2.get():
        if len(E2.get()) >= 6:
            e1V = E1.get()
            e2V = E2.get()
            yp = Toplevel(pencere)
            yp.geometry("200x250+600+250")
            yp.resizable(width=False,height=False)
            
            l1 = Label(yp,text="Kullanıcı Adı Giriniz(*)")
            l1.pack(padx=10,pady=10)
            
            e1 = Entry(yp,width=25)
            e1.pack(padx=10,pady=10)
            
            value = e1.get()
            E1.delete(0, END)
            E2.delete(0, END)
            messagebox.showinfo("Kayıt Ol", """Başarıyla Kaydolundu!
                                Gelen Ekrana Yeni Kullanıcı Adınızı Giriniz""")
           
            
            
            def kaydet():
                
                _cursor = connection.execute("SELECT * from User")
                boolean = True
                for _row in _cursor:
                    if _row[0] ==value:
                        boolean = False
                        messagebox.showwarning("Kullanıcı Adı","Bu Kullanıcı Adı Daha Önceden Alınmış")
                    break
        
                if boolean == True:
                    messagebox.showinfo("Kullanıcı Adı","Başarıyla Kaydolundu!")
                    connection.execute("INSERT INTO User (Email, Password, UserName) VALUES (?, ?, ?)", (e1V, e2V, e1.get()))
                    connection.commit()
                    connection.close()
                    pencere.destroy()
                    
                        
            
            b1 = Button(yp,text="Kaydet", fg="white", bg="#2185C5", activebackground="#1E6FA6", command=kaydet)
            b1.pack(padx=10,pady=10)
            
            
            
            
        else:            
            messagebox.showerror("Kayıt Ol", "Şifre En Az 6 Harf İçermeli")
    else:
        messagebox.showwarning("Kayıt Ol", "Lütfen Yıldızlı Yerlerin Tam Dolu Olduğundan Emin Olun")

def giris():
    yeni_pencere = Toplevel(pencere)
    yeni_pencere.title("Giriş Yap")

B1 = Button(pencere, text="Kayıt Ol", fg="white", bg="#2185C5", activebackground="#1E6FA6", command=kayitOl)
B1.place(relx=0.4, rely=0.5)

L5 = Label(pencere, text="Hesabınız Var Mı?", bg="#F9F6F2")
L6 = Label(pencere, text="Hemen Giriş Yapın", bg="#F9F6F2")

L5.place(relx=0.3, rely=0.7)
L6.place(relx=0.3, rely=0.77)

b2 = Button(pencere, text="Giriş Yap", bg="#2185C5", fg="white", activebackground="#1E6FA6", command=giris)
b2.place(relx=0.3, rely=0.87)



pencere.mainloop()