from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC
import random
from datetime import datetime, date, time
import webbrowser
#import mysql.connector 




class Inicio: 
    #  la función obtiene la ventana principal
    def __init__(self,ventanapeticion):
        # medidas de la ventana
        ventanapeticion.geometry('500x300')
        ventanapeticion.config(bd=20,bg="#8469AE")# borde exterior
        ventanapeticion.title("Pay-O")
        # Label 
        Label(ventanapeticion,text="Bienvenido a Pay-O",font=("Bahnschrift SemiBold Condensed",30,ITALIC,BOLD),bg="#E2C4E1",fg="#271F26",width="60",height=4,bd=12,relief=RAISED ).pack()
        # crear Boton que cuando se haga click empiece la función Usuario
        botonprimero=Button(ventanapeticion,text='Siguiente',command=self.Bancos)
        botonprimero.pack()


    def Bancos(self): 
        # Cerrar ventana 
        ventanapeticion.withdraw()
        #ventana Productos
        self.bancos=tk.Toplevel()
        # medidas de la ventana
        self.bancos.geometry('400x600')
        self.bancos.config(bd=20,bg="#8469AE")
        self.bancos.title("Bancos")
        # Label
        Label(self.bancos,text="Elige el Banco donde quieres pagar tu crédito",font=("Bahnschrift SemiBold Condensed",20,ITALIC,BOLD),bg="#E2C4E1",fg="#271F26",bd=10,relief=RAISED, width=60).pack()
        listbanco=LabelFrame(self.bancos, text="Lista de bancos permitidos", font=("Bodoni Bd BT", 12),bg="#9F5195", fg="white", relief=RIDGE, bd=10)
        listbanco.place(x=5, y=100,relwidth=1)

        Button(listbanco, text="Banco Colpatria", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black",command=self.Consultarcol).grid(row=0, column=0, padx=100, pady=10) 
        Button(listbanco, text="Banco Bancolombia", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black").grid(row=1, column=0, padx=100, pady=10)
        Button(listbanco, text="Banco Occiedente", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black",).grid(row=2, column=0, padx=100, pady=10) 

    def Datocuenta(self):
        # Cerrar ventana principal
        self.bancos.withdraw()
        self.datcl=tk.Toplevel()
        # medidas de la ventana
        self.datcl.geometry('400x400')
        self.datcl.config(bd=20,bg="#8469AE")
        self.datcl.title("Bancos")
        #variables
        self.numero_cuentaCol=StringVar()
        self.nombre_cliente = StringVar()
        # Este dato se Obtendría de la base de datos
        self.nombre_cliente.set(str("Ana María Lopez"))
        self.cedula=StringVar()
        # Este dato se Obtendría de la base de datos
        self.cedula.set(str("1272888382"))
        self.descripcion=StringVar()
        self.descripcion.set(str(" Crédito en Línea"))
        self.valorcol=IntVar()
        # Este dato se Obtendría de la base de datos
        self.valorcol.set(int(200000))
        self.interescol=DoubleVar()
        # Este dato se Obtendría de la base de datos
        self.interescol.set(0.02)
        self.fecha=StringVar()
        self.fecha.set(datetime.now())
        # self.cuentacl=Clientecuentas()
        # Label
        Label(self.datcl,text="Ingresa tus datos",font=("Bahnschrift SemiBold Condensed",20,ITALIC,BOLD),bg="#E2C4E1",fg="#271F26",bd=10,relief=RAISED, width=60).pack()

        datcliente=LabelFrame(self.datcl, text="Datos", font=("Bodoni Bd BT", 12),bg="#9F5195", fg="white", relief=RIDGE, bd=10)
        datcliente.place(x=5, y=100,relwidth=1)

        Label(datcliente, text="Ingresa El numero de tu cuenta", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black").grid(row=0, column=0, padx=10, pady=10) 
        Entry(datcliente, borderwidth=3, width=30,textvariable=self.numero_cuentaCol, bg="#E2C4E1", fg="black").grid(row=1, column=0, padx=10, pady=10)
        Button(datcliente,text='Siguiente',command=self.FacturaColp).grid(row=2, column=0, padx=10, pady=10)
    
       
    def Consultarcol(self):
        self.Datocuenta()
        # Por medio de este código se busca obtener la información en las bases de datos
        """n_cuenta=(self.numero_cuentacol.get(), )
        respuesta=self.cuentacl.encontrar(n_cuenta)
        if len(respuesta)>0:
            self.nombre_cliente.set(respuesta[0][0])
            self.cedula.set(respuesta[0][1])
            self.valor.set([0][2])
        else:
            self.nombre_cliente.se('')
            self.nombre_cliente.se('')
            messagebox.showinfo("error", "No existe un artículo con dicho código")"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def FacturaColp(self):
         # Cerrar ventana anterior
        self.datcl.withdraw()
        #  ventana Productos
        self.Vcol=tk.Toplevel()
        #  medidas de la ventana
        self.Vcol.geometry('1050x1000')
        self.Vcol.config(bd=20,bg="#8469AE")
        self.Vcol.title("Colpatria")
        # variables
        self.numero_facturaCol = StringVar()
        self.numero_facturaCol.set(str(random.randint(100,9999)))
        self.numero_cuentaCol=StringVar()

        # Label
        Label(self.Vcol,text="Colpatria Pago Crédito en Línea",font=("Bahnschrift SemiBold Condensed",20,ITALIC,BOLD),bg="#E2C4E1",fg="#271F26",bd=10,relief=RAISED, width=60).pack()

        #Datos del comprador
        datosCol=LabelFrame(self.Vcol, text="Datos del Cliente", font=("Bodoni Bd BT", 12),bg="#9F5195", fg="white", relief=RIDGE, bd=10)
        datosCol.place(x=0, y=100,relwidth=1)

        Label(datosCol, text="Nombre del Cliente", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black").grid(row=0, column=0, padx=20, pady=10)

        Entry(datosCol, borderwidth=3, width=30,textvariable=self.nombre_cliente,state=DISABLED).grid(row=0, column=1, padx=8)

        Label(datosCol, text="Cédula", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black",width=15).grid(row=1, column=0, padx=20,pady=15)

        Entry(datosCol, borderwidth=3, width=30,textvariable=self.cedula,state=DISABLED).grid(row=1, column=1, padx=8)

        Label(datosCol, text="Tipo de factura", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black",width=15).grid(row=2, column=0, padx=20,pady=15)

        Entry(datosCol, borderwidth=3, width=30,textvariable=self.descripcion,state=DISABLED).grid(row=2, column=1, padx=8)

        Label(datosCol, text="Fecha de elaboración", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black").grid(row=0, column=2, padx=40,pady=10)

        Entry(datosCol, borderwidth=3, width=30,textvariable=self.fecha,state=DISABLED).grid(row=0, column=3, padx=8)

        Label(datosCol, text="No.Factura", font=( "Bodoni Bd BT", 14), bg="#E2C4E1", fg="black",width=15).grid(row=1, column=2, padx=40,pady=15)

        Entry(datosCol, borderwidth=3, width=30,textvariable=self.numero_facturaCol,state=DISABLED).grid(row=1, column=3, padx=6)

        
        Button(datosCol, text="Generar Factura", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black",command=self.Factcolp).grid(row=2, column=3, padx=100, pady=10) 

        facturacionCol = Frame(self.Vcol, bd=5, relief=GROOVE, bg="#9F5195")
        facturacionCol.place(x=0, y=360, width=600, height=380)
        Label(facturacionCol, text="Facturación", font=("Bodoni Bd BT", 12,BOLD), bd=4, relief=SUNKEN, bg="#9F5195", fg="black").pack()
        scroll = Scrollbar(facturacionCol, orient=VERTICAL)
        self.textfactCol = Text(facturacionCol, yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.textfactCol.yview)
        self.textfactCol.pack(fill=BOTH, expand=1)

        Framepagocol = Frame(self.Vcol, bd=7, relief=GROOVE, bg="#5D33BD")
        Framepagocol.place(x=600, width=300, height=200,y=360)

        pagocol = Button(Framepagocol, text="Pagar", font=("Bodoni Bd BT", 15), bg="#E2C4E1", fg="black",width=15,command=self.MetoCol).grid(row=0, column=0, padx=15,pady=15)
        volvercol = Button(Framepagocol, text="Volver", font=("Bodoni Bd BT", 15), bg="#E2C4E1", fg="black", width=8, command=self.VenAtrascol).grid(row=1, column=0,padx=15,pady=15)

    def Factcolp(self):
        if (self.nombre_cliente.get() == "" or self.cedula.get() == ""):
            messagebox.showerror("Error", "Datos del Cliente incompletos")
        self.totin=self.valorcol.get()*self.interescol.get()
        self.totalcol=self.valorcol.get()+self.totin
        self.textfactCol.insert(END, "\t\t\tBienvenido a Pay-O\n")
        self.textfactCol.insert(END, "\t\t\tBanco Colpatria\n")
        self.textfactCol.insert(END, "\t\t\tCrédito en Línea\n")
        self.textfactCol.insert(END, f"\n\nNúmero de Factura: {self.numero_facturaCol.get()}")
        self.textfactCol.insert(END, f"\nNombre Cliente : {self.nombre_cliente.get()}")
        self.textfactCol.insert(END, f"\nCédula No. : {self.cedula.get()}")
        self.textfactCol.insert(END, "\n====================================================\n")
        self.textfactCol.insert(END, "\nDescripcion\t\tValor Solicitado\t\tInterés\t\tTotal \n")
        self.textfactCol.insert(END, "\n====================================================\n")
        self.textfactCol.insert(END, f"\nCrédito en Línea\t\t{self.valorcol.get()}\t\t{self.interescol.get()}\t\t{self.totalcol} \n")

    def VenAtrascol(self):
        #cerrar venatana 
        self.Vcol.withdraw()
        #LLamar a la funcion usuario nuevamente
        obj.Bancos()
        
    def Seleccionarcol(self):
       self.monitor.config(text="{}".format(self.opcionpagcol.get()))

    def MetoCol(self):
        self.Vcol.withdraw()
        self.metodocol=tk.Toplevel()
        #  medidas de la ventana
        self.metodocol.geometry('400x600')
        self.metodocol.config(bd=20,bg="#8469AE")
        self.metodocol.title("Pago Colpatria")
        Label(self.metodocol,text="Elige tu método de pago",font=("Bahnschrift SemiBold Condensed",20,ITALIC,BOLD),bg="#E2C4E1",fg="#271F26",bd=10,relief=RAISED, width=60).pack()
        # variables
        self.opcionpagcol = IntVar()
        Radiobutton(self.metodocol , text ="Tarjeta de crédito", variable=self.opcionpagcol,value=1,command=self.Seleccionarcol,font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black").pack()
        Radiobutton(self.metodocol , text ="PSE", variable=self.opcionpagcol,value=2,command=self.Seleccionarcol,font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black").pack()
        self.monitor=Label(self.metodocol)
        self.monitor.pack()
        Button(self.metodocol, text="Siguiente", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black",command=self.Pagocol).pack()

    def Pagocol(self):
        self.metodocol.withdraw()

        if self.opcionpagcol.get()==1:
            self.pagarcol=tk.Toplevel()
            self.pagarcol.geometry('400x600')
            self.pagarcol.config(bd=20,bg="#8469AE")
            self.pagarcol.title("Pago Colpatria TC")
            self.tipotarcol=StringVar()
            self.codsegcol=IntVar()
            Label(self.pagarcol,text="Realiza tu pago",font=("Bahnschrift SemiBold Condensed",20,ITALIC,BOLD),bg="#E2C4E1",fg="#271F26",bd=10,relief=RAISED, width=60).pack()

            frameCol=LabelFrame(self.pagarcol, text="Datos del pago", font=("Bodoni Bd BT", 12),bg="#9F5195", fg="white", relief=RIDGE, bd=10)
            frameCol.place(x=0, y=100,relwidth=1)

            Label(frameCol, text="Tipo de tarjeta(Visa, MasterCard)", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black").grid(row=0, column=0, padx=10, pady=10) 
            Entry(frameCol, borderwidth=3, width=30,textvariable=self.tipotarcol, bg="#E2C4E1", fg="black").grid(row=1, column=0, padx=10, pady=10)
            Label(frameCol, text="código de seguridad", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black").grid(row=2, column=0, padx=10, pady=10) 
            Entry(frameCol, borderwidth=3, width=30,textvariable=self.codsegcol, bg="#E2C4E1", fg="black").grid(row=3, column=0, padx=10, pady=10)
            Button(frameCol, text="Confirmar", font=("Bodoni Bd BT", 14), bg="#E2C4E1", fg="black",command=self.Confirmacioncol).grid(row=4, column=0, padx=10, pady=10)
        else:
            paginacol = webbrowser.get()
            paginacol.open("https://www.scotiabankcolpatria.com/personas/servicios/pagos/pagos-en-linea-pse")

    def Confirmacioncol(self):
        self.pagarcol.withdraw()   
        self.concol=tk.Toplevel()
        self.concol.geometry('400x200')
        self.concol.config(bd=20,bg="#8469AE")
        self.concol.title("Pago Confirmado")
        Label(self.concol,text="Pago Confirmado",font=("Bahnschrift SemiBold Condensed",20,ITALIC,BOLD),bg="#E2C4E1",fg="#271F26",bd=10,relief=RAISED, width=60).pack()

    
            





       


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Con esta clase se accede a la base de datos 
"""class Clientecuentas:
    def abrirsql(self):
        ingresarcu=mysql.connector.connect(host="localhost",user="root",passwd="", database="bd1")
        return ingresarcu

    def encontrar(self, n_cuenta):
        abrir=self.abrir()
        entrar=abrir.cursor()
        sql="select Nombre cliente, Cedula, Valor a pagar from cuentas where Numero de cuenta=%s"
        entrar.execute(sql, n_cuenta)
        abrir.close()
        return entrar.fetchall()"""

    


    
    



#  ventana principal
ventanapeticion=tk.Tk()
# objetp
obj=Inicio(ventanapeticion)
#se inicia el bucle
ventanapeticion.mainloop()


