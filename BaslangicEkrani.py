from tkinter import *
import TkGirisEkranı2
import TkKayitEkranı 

pencere = Tk()
pencere.title("Dexroly")
pencere.geometry("750x450+400+150")

pencere.resizable(width=False,height=False)
pencere.configure(bg="#F9F6F2")

giris = Canvas(pencere,bg='#C8CCCF')
giris.place(x=180,y=70)

L1 = Label(pencere,bg='#C8CCCF',text="Hesabınız Var mı?")
L1.place(x=250,y=100)

L2 = Label(pencere,bg='#C8CCCF',text="Hesabınız Yok mu?")
L2.place(x=250,y=180)

def oturumAc():
    pencere.destroy()
    
    TkGirisEkranı2.giris()

B1 = Button(pencere,text="Giriş Yap", bg="blue", fg="white", borderwidth=2, relief="raised",command=oturumAc)
B1.place(x=280,y=130)

def kaydol():
    pencere.destroy()
    TkKayitEkranı.kayit()

B2 = Button(pencere,text="Kaydol", bg="blue", fg="white", borderwidth=2, relief="raised",command=kaydol)
B2.place(x=290,y=210)



pencere.mainloop()
