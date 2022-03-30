from tkinter import *
from tkinter import messagebox as MessageBox
from Lenguaje import *

#alfabeto = list()

leng = Lenguaje()


def calcular_union():
    res = ''
    resultado.delete("1.0", "end")
    if (len(leng.lenguaje1) > 0 and len(leng.lenguaje2) > 0):
        res = leng.operacion_union()
        if (len(res) <= 0):
            res = "No hay elementos que mostrar"
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos lenguajes para realizar la union")  # título, mensaje
    resultado.insert(INSERT, res)

def calcular_intersecion():
    res = ''
    resultado.delete("1.0", "end")
    if (len(leng.lenguaje1) > 0 and len(leng.lenguaje2) > 0):
        res = leng.operacion_interseccion()
        if(len(res)<=0):
            res = "No hay elementos que mostrar"
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos lenguajes para realizar la interseccion")  # título, mensaje
    resultado.insert(INSERT, res)

def calcular_diferencia():
    res = ''
    resultado.delete("1.0", "end")
    if (len(leng.lenguaje1) > 0 and len(leng.lenguaje2) > 0):
        res = leng.operacion_diferencia()
        if (len(res) <= 0):
            res = "No hay elementos que mostrar"
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos lenguajes para realizar la diferencia")  # título, mensaje
    resultado.insert(INSERT, res)

def calcular_concatenacion():
    res = ''
    resultado.delete("1.0", "end")
    if (len(leng.lenguaje1) > 0 and len(leng.lenguaje2) > 0):
        res = leng.operacion_concatenacion()
        if (len(res) <= 0):
            res = "No hay elementos que mostrar"
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos lenguajes para realizar la concatenacion")  # título, mensaje
    resultado.insert(INSERT, res)

def calcular_cardinalidad():
    res = ""
    resultado.delete("1.0", "end")
    if (len(leng.lenguaje1) > 0 and len(leng.lenguaje2) > 0):
        res = leng.operacion_cardinalidad()
        if (len(res) <= 0):
            res = "No hay elementos que mostrar"
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos lenguajes para realizar la cardiinalidad")  # título, mensaje
    resultado.insert(INSERT, res)

def calcular_inversa():
    res = ""
    resultado.delete("1.0", "end")
    if (len(leng.lenguaje1) > 0 and len(leng.lenguaje2) > 0):
        res = leng.operacion_inversa()
        if (len(res) <= 0):
            res = "No hay elementos que mostrar"
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos lenguajes para realizar la inversa")  # título, mensaje
    resultado.insert(INSERT, res)

def calcular_potencia():
    res = ""
    resultado.delete("1.0", "end")
    if (len(leng.lenguaje1) > 0 and len(leng.lenguaje2) > 0):
        pass
    else:
        MessageBox.showinfo("Aviso!", "Deben existir dos lenguajes para realizar la inversa")  # título, mensaje
    resultado.insert(INSERT, res)

def insertar_palabra_1():
    alfabeto = list()
    letra = entry.get()
    if(len(letra) >= 1):
        if(leng.add_elemento_1(letra)):
            MessageBox.showinfo("Aviso!", "Palabra insertada con exito")  # título, mensaje
            entry.delete(0,"end")
            MessageBox.showinfo("Aviso!", ("Lenguaje ", leng.lenguaje1))  # título, mensaje
        else:
            MessageBox.showinfo("Error!", "La palabra no pudo ser insertado porque ya existe")  # título, mensaje
            entry.delete(0, "end")
    else:
        MessageBox.showinfo("Error!", "Se recomienda escribir una palabra de al menos un caracter")  # título, mensaje

def insertar_palabra_2():
    alfabeto = list()
    letra = entry2.get()
    if (len(letra) >= 1):
        if (leng.add_elemento_2(letra)):
            MessageBox.showinfo("Aviso!", "Palabra insertada con exito")  # título, mensaje
            entry2.delete(0, "end")
            MessageBox.showinfo("Aviso!", ("Lenguaje ", leng.lenguaje2))  # título, mensaje
        else:
            MessageBox.showinfo("Error!", "La palabra no pudo ser insertado porque ya existe")  # título, mensaje
            entry2.delete(0, "end")
    else:
        MessageBox.showinfo("Error!","Se recomienda escribir una palabra de al menos un caracter")  # título, mensaje

                #se crea la ventana

root = Tk()
root.geometry("420x480")
root.title("Taller 4 (Lenguaje)")
root['bg'] = '#c9c9c9'
root.resizable(False, False)
#se crea el frame
frame = Frame(root, bg='#c9c9c9', relief="raised", width=414, height=588)
frame.grid(column=0, row=0, padx=3, pady=6)
#se crea el titulo
lbl_titulo = Label(frame, text="LENGUAJES", font=("Arial", 15), width=20)
lbl_titulo['bg'] = '#c9c9c9'
lbl_titulo.place(x=105, y=12)
#se crea la entrada del alfabeto
lbl_palabra1 = Label(frame, text="Digite una palabra")
lbl_palabra1['bg'] = '#c9c9c9'
lbl_palabra1.place(x=50, y=66)
entry = Entry(frame, width=12, font=("Arial", 12))
entry.place(x=152, y=60)
#boton insertar alfabeto
btn_insertar = Button( text="Insertar", width=8, command=insertar_palabra_1)
btn_insertar.place(x=290, y=64)

lbl_palabra2 = Label(frame, text="Digite una palabra")
lbl_palabra2['bg'] = '#c9c9c9'
lbl_palabra2.place(x=50, y=111)
entry2 = Entry(frame, width=12, font=("Arial", 12))
entry2.place(x=152, y=105)
#boton insertar alfabeto
btn_insertar2 = Button( text="Insertar", width=8, command=insertar_palabra_2)
btn_insertar2.place(x=290, y=109)

#se crea un label calcular
lbl_calcular = Label(frame, text="Calcular", font=("Arial", 12))
lbl_calcular['bg'] = '#c9c9c9'
lbl_calcular.place(x=177, y=150)
#se crean los botones
btn_un = Button( text="Union", width=18, command=calcular_union)
btn_un.place(x=50, y=195)
btn_difer = Button( text="Direfencia", width=18, command=calcular_diferencia)
btn_difer.place(x=230, y=195)
btn_inter = Button( text="Intersección", width=18, command=calcular_intersecion)
btn_inter.place(x=50, y=230)
btn_conca = Button( text="Concatenacion", width=18, command=calcular_concatenacion)
btn_conca.place(x=230, y=230)
btn_cardi = Button( text="Cardinalidad", width=18, command=calcular_cardinalidad)
btn_cardi.place(x=50, y=265)
btn_cardi = Button( text="Inversa", width=18, command=calcular_inversa)
btn_cardi.place(x=230, y=265)
btn_cardi = Button( text="Potencia", width=18, command=calcular_potencia)
btn_cardi.place(x=50, y=300)
#se crea el cuadro de texto donde se visualizan los resultados
resultado = Text(frame, width=43, height=6, font=("Arial", 12))
resultado.place(x=10, y=350)

root.mainloop()