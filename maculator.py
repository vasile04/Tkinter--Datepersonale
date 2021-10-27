# Sa se creeze un program care afiseaza o fereastr cu titlul Chestionar
# trebuie sa contina:
# Numele, prenumele
# Data nasterii
# Locul de studii/ munca
# Hobby
from tkinter import *
from tkinter import font
chestionar2 = Tk()
chestionar2.geometry('400x400')
np = Label(chestionar2, text='Introdu numele prenumele: ' , font=('Calibri', 23, font.BOLD))
np.grid(column=0, row=0)
np1 = Entry(chestionar2, width=24)
np1.grid(column=1, row=0)
dt= Label(chestionar2, text='Introdu data nasterii: ', font=('calibri', 23, font.BOLD))
dt.grid(column=0, row=1)
d1 = Spinbox(chestionar2, from_=1, to=31 )
d1.grid(column=1, row=1)
d2=Spinbox(chestionar2, from_=1, to=12)
d2.grid(column=3, row=1)
d3=Spinbox(chestionar2, from_=1978, to=2021)
d3.grid(column=4, row=1)
hbby=Label(chestionar2, text='scrie ce hobby-uri ai: ', font=('Calibri',23, font.BOLD ))
hbby.grid(column=0, row=2)
hbb1 = Text(chestionar2, width=45, height=15, bg='white')
hbb1.grid(column=1, row=2)
s1=Button(chestionar2, text='Trimite')
s1.place(x=500, y=380)
chestionar2. mainloop()