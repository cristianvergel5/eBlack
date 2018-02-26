#import win32com.client as clwin

#def SapiLee(lectura):
	#habla = clwin.Dispatch("SAPI.SpVoice")
	#habla.Speak(lectura)

def leer_eBlack(name):

	if name.find(".eb") == False:
		name = name + ".eb"

	try:

		with open(name, "r") as archivo:
			for line in archivo:
				print(line)

	except:
		print("No existe un archivo eBlack con ese nombre, asegurese de que tenga extension .eb")
	
class lexer_eBlack():

	def __init__(self, dictionary, filename):
		self.__dictionary = dictionary
		self.__filename = filename
		self.__tokens = []

	@property
	def dictionary(self):
		return self.__dictionary

	@dictionary.setter
	def dictionary(self, dictionary):
		self.__dictionary = dictionary

	def dictionary(self):
		self.__dictionary = None

	@property
	def filename(self):
		return self.__dictionary

	@filename.setter
	def filename(self, filename):
		self.__filename = filename

	@property
	def tokens(self):
		return self.__tokens

	@tokens.setter
	def tokens(self, token):
		self.__tokens.append(token)

	def obtenerToken(self, simbolo):

		simbolo = simbolo.lower()
		simbolo = simbolo.rstrip("\n")
		parecido = ""
		tipo = ""

		try:

			with open(self.__dictionary, "r") as diccionario:
				
				for linea in diccionario:

					linea = linea.rstrip("\n")

					#print(simbolo.find(linea))

					if simbolo.find(linea) == 0:
						parecido = linea
						#print("La linea es " + linea + " y parecido es: " + parecido)

					if linea.isupper():
						tipo = linea

					else:
						if linea == simbolo:
							tipo = tipo.rstrip("\n")
							simbolo = simbolo.rstrip("\n")
							return True, "["+tipo+", "+simbolo+"]"	

			print(simbolo)
			return False, parecido

		except:
			print("Ha ocurrido un error, puede que sea el archivo diccionario de eBlack, revisar")


	def leerPrograma(self):

		if self.__filename != None:

			contador = 1
			lista = []

			try:

				with open(self.__filename, "r") as archivo:

					for linea in archivo:
						
						lista = linea.split(" ")

						for i in lista:

							valor, resultado = self.obtenerToken(i)

							if valor == False:
								self.tokens = "Error en la linea " + str(contador) + " quiso decir "+ str(resultado)
								#return activar el return para salir del programa cuando encuentre un error
							else:
								self.tokens = str(resultado) + " Linea: " + str(contador)

						contador = contador + 1

			except:
				print("Ha ocurrido un error en el proceso de lectura del programa eBlack")

#SapiLee("Inicio de lexer eBlack")
eBlack = lexer_eBlack("Dictionary_eBlack.eb", "prueba.eb")
eBlack.leerPrograma()
Resultado = eBlack.tokens
for i in Resultado:
	print(i)
#	SapiLee(i)

#SapiLee("Fin de lexer eBlack")
#abrirArch_eBlack("Dictionary_eBlack.eb")
