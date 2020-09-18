import socket
import threading
import sys
import pickle
import tkinter
from tkinter import * 

class Cliente():
	my_msj='error'
	caja_salida='?'
	
	"""docstring for Cliente"""
	def __init__(self, host="localhost", port=4000):
		#conexion al puerto
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target=self.msg_recv)
		#print(msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		#identificacion de usuario
		Nombre=input("introduce tu nombre>>>")
		if Nombre=='':
			Nombre='usuario'

		print("*****ya puedes cerrar esta pantalla****")
	#	inicio de la
		ventana=tkinter.Tk()
		ventana.geometry("563x432")
		#titulo de la ventana 
		ventana.title("Pychat GUI V.0.2")

		#fondo de pantalla otacon
		fondo=PhotoImage(file="IMG/base_real.png")
		imagen=Label(ventana,image=fondo).place(x=0,y=0)

		#letras en pantalla :
		nombre=tkinter.Label(ventana,text="Pychat GUI V.0.2").place(x=200,y=10)

		#para sacar los mensajes de la caja 
		global my_msj
		my_msj=tkinter.StringVar()

		#caja de entrada :
		escribe_tu_msg=tkinter.Label(ventana,text="escribe tu mensaje aca :",bg="gray").place(x=22,y=280)
		caja_entrada=tkinter.Entry(ventana,borderwidth=0,width=62,textvariable=my_msj)
		caja_entrada.place(x=22,y=300)


		#barra para moverte a travez de los mensajes 
		barra=tkinter.Scrollbar()
		barra.place(x=310,y=230)


		#caja de salida :
		global caja_salida


		caja_salida=tkinter.Listbox(height=12,width=43,bg="gray",borderwidth=0,yscrollcommand=barra.set)
		caja_salida.place(x=18,y=57)


		

		#boton de envio :
		envio=tkinter.Button(ventana,text="Enviar",padx=10,pady=14,bg="red",command=lambda:self.send_msg(Nombre+" >>"+my_msj.get()))
		envio.place(x=465,y=280)

		#animacion de otacon 
		otacon=PhotoImage(file="IMG/otacon.png")
		otakon=Label(ventana,image=otacon).place(x=400,y=50)

			
		#usuario :
		user=tkinter.Button(ventana,text="usuario",padx=8,pady=15,bg="blue",command=lambda:print("esto por el momento no hace nada \n te recomiendo cerrar esta ventana "))
		user.place(x=465,y=335)

		#usuario actual 
		usr_act=tkinter.Label(ventana,text="usuario actual :"+Nombre,bg="gray")
		usr_act.place(x=20,y=330)		


#		ID=input("identificate >>>")
		#while True:
		#	msg = input('->')
		#	if msg != 'salir':
		#		self.send_msg(Nombre+">>"+msg)
		#	else:
		#		self.sock.close()
		#		sys.exit()
		ventana.mainloop()

	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					a=pickle.loads(data)
					#print(a)
					caja_salida.insert(tkinter.END,a)
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))
		#print(msg)
		my_msj.set("")
		caja_salida.insert(tkinter.END,msg)

c = Cliente()