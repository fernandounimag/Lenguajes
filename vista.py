from tkinter import *
from Alfabeto import *
from tkinter import messagebox as MessageBox

def calcular_union():
    res = ''
    resultado.delete("1.0","end")
    if(entry1.get() != '' and entry2.get() != ''):
        alfabetos = Alfabeto()
        a1 = list(entry1.get())
        a2 = list(entry2.get())
        alfabetos.set_alfabeto1(a1)
        alfabetos.set_alfabeto2(a2)
        res = alfabetos.union()
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos alfabetos para realizar la union")  # título, mensaje
    resultado.insert(INSERT,res)

def calcular_intersecion():
    res = ''
    resultado.delete("1.0", "end")
    if(entry1.get() != '' and entry2.get() != ''):
        alfabetos = Alfabeto()
        a1 = list(entry1.get())
        a2 = list(entry2.get())
        alfabetos.set_alfabeto1(a1)
        alfabetos.set_alfabeto2(a2)
        res = alfabetos.interseccion()
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos alfabetos para realizar la interseccion")  # título, mensaje
    resultado.insert(INSERT, res)

def calcular_diferencia():
    res = ''
    resultado.delete("1.0", "end")
    if(entry1.get() != '' and entry2.get() != ''):
        alfabetos = Alfabeto()
        a1 = list(entry1.get())
        a2 = list(entry2.get())
        alfabetos.set_alfabeto1(a1)
        alfabetos.set_alfabeto2(a2)
        res = alfabetos.diferencia()
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos alfabetos para realizar la diferencia")  # título, mensaje
    resultado.insert(INSERT, res)

def calcular_estrella():
    res = ''
    resultado.delete("1.0", "end")
    if (entry1.get() != '' or entry2.get() != ''):
        alfabetos = Alfabeto()
        a1 = list(entry1.get())
        a2 = list(entry2.get())
        alfabetos.set_alfabeto1(a1)
        alfabetos.set_alfabeto2(a2)
        res = alfabetos.estrella1()
    else:
        MessageBox.showinfo("Aviso!", "Deben existir al menos un alfabeto para calcular su estrella")  # título, mensaje
    resultado.insert(INSERT, res)

#se crea la ventana
root = Tk()
root.geometry("420x420")
root.title("Taller 4 (Alfabeto)")
root['bg'] = '#c9c9c9'
root.resizable(False, False)
#se crea el frame
frame = Frame(root, bg='#c9c9c9', relief="raised", width=414, height=588)
frame.grid(column=0, row=0, padx=3, pady=6)
#se crea el titulo
lbl_titulo = Label(frame, text="ALFABETOS", font=("Arial", 15), width=20)
lbl_titulo['bg'] = '#c9c9c9'
lbl_titulo.place(x=105, y=12)
#se crea la primera entrada y su label
lbl_palabra1 = Label(frame, text="Digite un alfabeto")
lbl_palabra1['bg'] = '#c9c9c9'
lbl_palabra1.place(x=50, y=70)
entry1 = Entry(frame, width=35)
entry1.place(x=150, y=70)
#se crea la segunda entrada y su label
lbl_palabra2 = Label(frame, text="Digite un alfabeto")
lbl_palabra2['bg'] = '#c9c9c9'
lbl_palabra2.place(x=50, y=100)
entry2 = Entry(frame, width=35)
entry2.place(x=150, y=100)
#se crea un label calcular
lbl_calcular = Label(frame, text="Calcular", font=("Arial", 12))
lbl_calcular['bg'] = '#c9c9c9'
lbl_calcular.place(x=177, y=130)
#se crean los botones
btn_un = Button( text="Union", width=18, command=calcular_union)
btn_un.place(x=50, y=175)
btn_difer = Button( text="Direfencia", width=18, command=calcular_diferencia)
btn_difer.place(x=230, y=175)
btn_inter = Button( text="Intersección", width=18, command=calcular_intersecion)
btn_inter.place(x=50, y=210)
btn_estre = Button( text="Estrella", width=18, command=calcular_estrella)
btn_estre.place(x=230, y=210)
#se crea el cuadro de texto donde se visualizan los resultados
resultado = Text(frame, width=43, height=8, font=("Arial", 12))
resultado.place(x=10, y=250)

root.mainloop()