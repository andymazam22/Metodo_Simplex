from tkinter import *
raiz = Tk()


barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300,height=300)
metodoSimplexMenu=Menu(barraMenu)
proyectoMenu=Menu(barraMenu)
salirMenu=Menu(barraMenu)

barraMenu.add_cascade(label="Metodo Simplex", menu=metodoSimplexMenu)
barraMenu.add_cascade(label="Proyectos", menu=proyectoMenu)
barraMenu.add_cascade(label="Salir", menu=salirMenu)
raiz.mainloop()