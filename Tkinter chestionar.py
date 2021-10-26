# Sa se creeze un program care afiseaza o fereastr cu titlul Chestionar
# trebuie sa contina:
# Numele, prenumele
# Data nasterii
# Locul de studii/ munca
# Hobby
from tkinter import *
from tkinter import font

chestionar=Tk()
chestionar.title('Chestionar personal:')
chestionar.geometry('400x400')
Np=Label(chestionar, text="Numele prenumele: " ,font=('Times New Roman', 27))
Np.grid(column=0, row=0)
np1=Entry(chestionar, width=23, bg='red')
np1.grid(column=1, row=0)
dt=Label(chestionar, text='Data nasterii' ,font=('Times New Roman', 27))
dt.grid(column=0, row=1)
dt1=Entry(chestionar, width=23, background='cyan')
dt1.grid(column=1, row=1)
lc=Label(chestionar, text='Locul de munca sau studii: ', font=('Times New Roman', 27))
lc.grid(column=0, row=2)
lc1=Entry(chestionar, width=23)
lc1.grid(column=1, row=2)
hbby=Label(chestionar, text='Ce hobby-uri ai? ', font=('Times New Roman', 27))
hbby.grid(column=0, row=3)
hbby1=Entry(chestionar, width=100)
hbby1.grid(column=1, row=3)
s1=Button(chestionar, text='Trimite', font=('Calibri', 15, font.BOLD))
s1.grid(column=3, row=20)
chestionar.mainloop()