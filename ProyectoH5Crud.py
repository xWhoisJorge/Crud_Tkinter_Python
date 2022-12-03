from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
from PIL import ImageTk, Image
import openpyxl


##### En esta 1er ventana se hace el Login #####
root = Tk()
root.title("login")
root.geometry("800x640")

#Quitamos la barra/iconos minimizar/maximizar/Cerrar, para obligar a usar los botos creados
root.overrideredirect(True)

imagenlogin = ImageTk.PhotoImage(Image.open("imglogin.png"))
Labellog = Label(image=imagenlogin)
Labellog.config(width=0,height=0, background="#404258")
Labellog.pack()
Labellog.grid()

##### Para ajustar la ventana al centro de la pantalla, obenemos el ancho y largo #####
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
#Guardamos el largo y alto de la ventana
wventana = 800
hventana = 640
#Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
# Se lo aplicamos a la geometría de la ventana
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

def Login():
    miUsuario = usuario.get()
    miContraseña = contraseña.get()
    
    if (miUsuario == "" and miContraseña == ""):
        messagebox.showinfo("Error","Rellene los campos por favor")
        
    elif (miUsuario == "123" and miContraseña == "123"):
        messagebox.showinfo("Conectado","Usuario Correcto")
        root.destroy()
        
    else:
        messagebox.showinfo("Error","Usuario incorrecto, por seguridad se cerrará")
        exit(1)

global  usuario
global  contraseña

##### Etiquetas, entradas y Boton para el Login #####

usuario=Label (root, text="U  S  E  R",font=("Arial",10,"bold"), background="#FEFCF3", fg="#313131").place(x=280,y=300)
usuario=Entry(root, background="#FEFCF3", fg="#313131")
usuario.place(x=420, y=300)
contraseña=Label (root, text="P A S S W O R D",font=("Arial",10,"bold"), background="#FEFCF3", fg="#313131").place(x=280, y=350)
contraseña=Entry(root, background="#FEFCF3", fg="#313131")
contraseña.place(x=420, y=350)
contraseña.config(show="*")
Titulo=Label (root, text="PROYECTO FINAL PROG II - C.R.U.D - SISTEMA DE INVENTARIO",font=("Arial",10), background="#313131", fg="#FEFCF3").place(x=200, y=600)

Button(root, text="LOGIN",font=("Arial",10,"bold"), background="#313131", fg="#FEFCF3", command=Login, height=3, width=13).place(x=350,y=400)
root.mainloop()

##### En esta 2da pantalla se rellena la base de datos #####
root=Tk()
root.title("Tiendita Ilegal")
root.geometry("800x640")
root.config(bg="#404258")
root.resizable(0,0) 
root.overrideredirect(True)

wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
wventana = 800
hventana = 640
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

imagen = ImageTk.PhotoImage(Image.open("imgbg.png"))
Label1 = Label(image=imagen, width=795, height=635 )
Label1.pack()
Label1.grid()

ProductID=StringVar()
categoria=StringVar()
nombreprod=StringVar()
preciounitario=StringVar()
cantidadstock=StringVar()
plataforma=StringVar()
tipo=StringVar()

##### Conectamos al archivo de base de datos #####
def Conexion():
    miConexion=sqlite3.connect("InventarioBD.db")
    miCursor=miConexion.cursor()
    try: 
        miCursor.execute('''
            CREATE TABLE INVENTARIO (
            ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
            CATEGORIA VARCHAR(50),
            NOMBREPROD VARCHAR(50),
            PRECIOUNITARIO VARCHAR(50),
            CANTIDADSTOCK VARCHAR(50),
            PLATAFORMA VARCHAR(50),
            TIPO VARCHAR(50))  
            ''')        
        messagebox.showinfo("BBDD","La Base de Datos ha sido creada.")
    
    except:
        messagebox.showwarning("ERROR","Esta Base de Datos ya existe.")
    
def eliminarTabla():
	miConexion=sqlite3.connect("InventarioBD.db")
	miCursor=miConexion.cursor()
	if messagebox.askyesno(message="¿Los Datos se perderan definitivamente, Desea continuar?", title="ADVERTENCIA"):
		miCursor.execute("DROP TABLE INVENTARIO")
	else:
		pass

def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Desea cerrar el programa?")
    if valor=="yes":
        root.destroy()
        
def limpiarCampos():
    categoria.set("")
    nombreprod.set("")
    preciounitario.set("")
    cantidadstock.set("")
    plataforma.set("")
    tipo.set("")
def Licencia():
    messagebox.showinfo("Licencia",
    '''
        C.R.U.D 
        PROGRAMACIÓN II 
        PRODUCT LICENSE V. 1.0
    ''')
def Acerca():
    messagebox.showinfo("Acerca de",
    '''
        El objetivo es: 
        Almacenar, Organizar y Clasificar los datos ingresados.
    ''')
    
def crear():
    miConexion=sqlite3.connect("InventarioBD.db")
    miCursor=miConexion.cursor()
    
    datos=categoria.get(),nombreprod.get(),preciounitario.get(),cantidadstock.get(),plataforma.get(),tipo.get()
    miCursor.execute("INSERT INTO INVENTARIO VALUES(NULL,?,?,?,?,?,?)", (datos))
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con éxito")
    pass
    limpiarCampos()
    mostrartodoslosdatos()
    
def leer():
    
    '''miConexion=sqlite3.connect("InventarioBD.db")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM INVENTARIO WHERE ProductID=" +ProductID.get())
    elinventario=miCursor.fetchall()
    
    for inventario in elinventario:
        ProductID.set(inventario[0])
        codigoprod.set(inventario[1])
        Nombreprod.set(inventario[2])
        cantidad.set(inventario[3])
        preciounidad.set(inventario[4])
        procedencia.set(inventario[5])
        estado.set(inventario[6])
    miConexion.commit()'''
    messagebox.showerror(message="Esta opción está desabilitada en el codigo", title="Error")

def actualizar():
    
    miConexion=sqlite3.connect("InventarioBD.db")
    miCursor=miConexion.cursor()
    datos=categoria.get(),nombreprod.get(),preciounitario.get(),cantidadstock.get(),plataforma.get(),tipo.get()
    miCursor.execute("UPDATE INVENTARIO SET CATEGORIA=?, NOMBREPROD=?, PRECIOUNITARIO=?, CANTIDADSTOCK=?, PLATAFORMA=?, TIPO=? "+
    "WHERE PRODUCTID=" + ProductID.get(),(datos))
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con éxito")
    pass
    limpiarCampos()
    mostrartodoslosdatos()
    
def borrar():
    
    miConexion=sqlite3.connect("InventarioBD.db")
    miCursor=miConexion.cursor()
    
    try:
        if messagebox.askyesno(message="¿Realmente desea eliminar este Registro?", title="Advertencia"):
            miCursor.execute("DELETE FROM INVENTARIO WHERE PRODUCTID=" +ProductID.get())
            miConexion.commit()
    except:
        messagebox.showwarning("Advertencia","Ocurrió un error")
        pass
    limpiarCampos()
    mostrartodoslosdatos()
    
def mostrartodoslosdatos():
	miConexion=sqlite3.connect("InventarioBD.db")
	miCursor=miConexion.cursor()
	Inventario=tree.get_children()
	for Inventario in Inventario:
		tree.delete(Inventario)
	try:
		miCursor.execute("SELECT * FROM INVENTARIO")
		for row in miCursor:
			tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
	except:
		pass

def borrarRegistro():
    miConexion=sqlite3.connect("InventarioBD.db")
    miCursor=miConexion.cursor()
    
    try:
        if messagebox.askyesno(message="¿Realmente desea eliminar este Registro?", title="Advertencia"):
            miCursor.execute("DELETE FROM INVENTARIO WHERE productID=" +ProductID.get())
            miConexion.commit()
    except:
        messagebox.showwarning("Advertencia","Para Eliminar un Registro primero debes darle Dobleclick")
        pass
    limpiarCampos()
    mostrartodoslosdatos()

###### Treeview permite crear una vista de tablas o datos ingresados ######

tree=ttk.Treeview(height=8,columns=('#0','#1','#2','#3','#4','#5'))
tree.place(x=25, y=405)
tree.heading('#0', text="#", anchor=SW)
tree.column('#0',width=50)
tree.heading('#1', text="Categoria", anchor=SW)
tree.column('#1',width=100)
tree.heading('#2', text="Nombre Prod", anchor=SW)
tree.column('#2',width=140)
tree.heading('#3', text="Precio Unitario", anchor=SW)
tree.column('#3',width=120)
tree.heading('#4', text="Cantidad en Stock", anchor=SW)
tree.column('#4',width=120)
tree.heading('#5', text="Plataforma", anchor=SW)
tree.column('#5',width=120)
tree.heading('#6', text="Tipo", anchor=SW)
tree.column('#6',width=100)

#Este evento funciona para editar un registro dando Dobleclick. Sin necesidad de ingresar datos para buscarlo
def seleccionarUsandoClick(event):
	item=tree.identify('item',event.x,event.y)
	ProductID.set(tree.item(item,"text"))
	categoria.set(tree.item(item,"values")[0])
	nombreprod.set(tree.item(item,"values")[1])
	preciounitario.set(tree.item(item,"values")[2])
	cantidadstock.set(tree.item(item,"values")[3])
	plataforma.set(tree.item(item,"values")[4])
	tipo.set(tree.item(item,"values")[5])
    
tree.bind("<Double-1>", seleccionarUsandoClick)

def GuardarExcel():
#Seleccionamos el archivo a convertir en Excel
    DBFILE = "InventarioBD.db"
    
#Nos conectamoms a la BBDD y creamos el archivo
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    book = openpyxl.Workbook()
    sheet = book.active
    
#Exportamos los datos a Excel
    cursor.execute("SELECT * FROM `Inventario`")
    results = cursor.fetchall()
    i = 0
    for row in results:
        i += 1
        j = 1
        for col in row:
            cell = sheet.cell(row = i, column = j)
            cell.value = col
            j += 1
            
#Guardamos el archivo en formato excel
    if messagebox.askyesno("Guardando", "¿Desea guardar en Formato Excel esta Base de datos?"):
        book.save("InventarioBD.xlsx")
    else:
        pass
        
###### Creamos la barra y zona de Menús ######
menubar=Menu(root)
menubasedat=Menu(menubar, tearoff=0)
menubasedat.add_command(label="Conectar/Crear BBDD", command=Conexion)
menubasedat.add_command(label="Eliminar Tabla de Datos", command=eliminarTabla)
menubasedat.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="BBDD", menu=menubasedat)

menuborrar=Menu(menubar, tearoff=0)
menuborrar.add_command(label="Limpiar campos", command=limpiarCampos)
menubar.add_cascade(label="Limpiar",menu=menuborrar )

crud=Menu(menubar, tearoff=0)
crud.add_command(label="Añadir", command=crear)
crud.add_command(label="Leer", command=leer)
crud.add_command(label="Actualizar", command=actualizar)
crud.add_command(label="Borrar", command=borrar)
menubar.add_cascade(label="CRUD", menu=crud)

ayudamenu=Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Licencia", command=Licencia)
ayudamenu.add_command(label="Acerca", command=Acerca)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)
root.config(menu=menubar)

###### Creamos las Etiquetas para cada campo a rellenar ######

'''LabelBuscar=Label(root, text="ID ",font=("Arial",10, "bold"))
LabelBuscar.grid(column=0, row=1)
LabelBuscar.place(x=280,y=50, width=120, height=20)'''

Labelcodigoprod=Label(root, text="Categoria: ",font=("Arial",10, "bold"), bg="#313131", fg="#FEFCF3")
Labelcodigoprod.grid(column=0, row=1)
Labelcodigoprod.place(x=280,y=90, width=120, height=20)

LabelNombreprod=Label(root, text="Nombre Prod: ",font=("Arial",10, "bold"), bg="#313131", fg="#FEFCF3")
LabelNombreprod.grid(column=0, row=2)
LabelNombreprod.place(x=280,y=120, width=120, height=20)

LabelCantidad=Label(root, text="Precio Unitario: ",font=("Arial",10, "bold"), bg="#313131", fg="#FEFCF3")
LabelCantidad.grid(column=0, row=3)
LabelCantidad.place(x=280,y=150, width=120, height=20)

LabelPreciounidad=Label(root, text="Cantidad en Stock: ",font=("Arial",10, "bold"), bg="#313131", fg="#FEFCF3")
LabelPreciounidad.grid(column=0, row=4)
LabelPreciounidad.place(x=280,y=180, width=120, height=20)

LabelProcedencia=Label(root, text="Plataforma: ",font=("Arial",10, "bold"), bg="#313131", fg="#FEFCF3")
LabelProcedencia.grid(column=0, row=5,sticky=W)
LabelProcedencia.place(x=280,y=210, width=120, height=20)

LabelEstado=Label(root, text="Tipo: ",font=("Arial",10, "bold"), bg="#313131", fg="#FEFCF3")
LabelEstado.grid(column=0, row=5,sticky=W)
LabelEstado.place(x=280,y=240, width=120, height=20)

###### Creamos los campos a rellenar ######

'''EntryBuscar=Entry(root, textvariable=ProductID, width=16,font=("Arial",12))
EntryBuscar.grid(column=1, row=1)
EntryBuscar.place(x=420,y=50, width=120, height=20)'''

EntryCodigoprod=Entry(root, textvariable=categoria, width=16,font=("Arial",10, "bold"), bg="#525252", fg="#FEFCF3")
EntryCodigoprod.grid(column=1, row=1)
EntryCodigoprod.place(x=420,y=90, width=120, height=20)

EntryNombreprod=Entry(root, textvariable=nombreprod, width=10,font=("Arial",10, "bold"), bg="#525252", fg="#FEFCF3")
EntryNombreprod.grid(column=1, row=2)
EntryNombreprod.place(x=420,y=120, width=120, height=20)

EntryCantidad=Entry(root,textvariable=preciounitario,font=("Arial",10, "bold"), bg="#525252", fg="#FEFCF3")
EntryCantidad.grid(column=1, row=3)
EntryCantidad.place(x=420,y=150, width=120, height=20)

EntryPreciounidad=Entry(root,textvariable=cantidadstock,font=("Arial",10, "bold"), bg="#525252", fg="#FEFCF3")
EntryPreciounidad.grid(column=1, row=4)
EntryPreciounidad.place(x=420,y=180, width=120, height=20)

Entryprocedencia=Entry(root,textvariable=plataforma,font=("Arial",10, "bold"), bg="#525252", fg="#FEFCF3")
Entryprocedencia.grid(column=1, row=5)
Entryprocedencia.place(x=420,y=210, width=120, height=20)

EntryEstado=Entry(root,textvariable=tipo,font=("Arial",10, "bold"), bg="#525252", fg="#FEFCF3")
EntryEstado.grid(column=1, row=5)
EntryEstado.place(x=420,y=240, width=120, height=20)

###### Creamos los Botones ######

BotonCrear=Button(root, text="Crear Registro", command=crear,font=("Arial",9, "bold"), bg="#313131", fg="#FEFCF3")
BotonCrear.place(x=170,y=300)

BotonLeer=Button(root, text="Limpiar Campos", command=limpiarCampos,font=("Arial",9, "bold"), bg="#313131", fg="#FEFCF3")
BotonLeer.place(x=275,y=300)

BotonActualizar=Button(root, text="Actualizar Registro", command=actualizar,font=("Arial",9, "bold"), bg="#313131", fg="#FEFCF3")
BotonActualizar.place(x=390,y=300)

BotonBorrar=Button(root, text="Borrar Registro", command=borrar,font=("Arial",9, "bold"), bg="#313131", fg="#FEFCF3")
BotonBorrar.place(x=520,y=300)

BotonMostrartodo=Button(root, text="Leer Base de Datos Completa", command=mostrartodoslosdatos,font=("Arial",9, "bold"), bg="#313131", fg="#FEFCF3")
BotonMostrartodo.place(x=150, y=370)

BotonEliminarRegistro=Button(root, text="Eliminar Registro Seleccionado",bg="#CA3E47", fg="white", command=borrarRegistro,font=("Arial",9, "bold"))
BotonEliminarRegistro.place(x=340, y=370)

BotonEliminarRegistro=Button(root, text="Guardar en Excel",bg="Green", fg="white", command=GuardarExcel,font=("Arial",9, "bold"))
BotonEliminarRegistro.place(x=540, y=370)



root.mainloop()