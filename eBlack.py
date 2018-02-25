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

	def __init__(self, dictionary, filename, tokens):
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

		simbolo = simbolo.lower() + "\n"
		tipo = ""

		try:

			with open(self.__dictionary, "r") as diccionario:
				
				print("Prueba Dictionary_eBlack.eb: ", self.__dictionary)

				for linea in diccionario:

					if str(linea) == "PALABRA RESERVADA\n" or str(linea) == "OPERADOR\n":
						tipo = linea

					else:
						if linea == simbolo:
							tipo = tipo.rstrip("\n")
							simbolo = simbolo.rstrip("\n")
							return "["+tipo+", "+simbolo+"]"		

		except:
			print("Ha ocurrido un error, puede que sea el archivo diccionario de eBlack, revisar")

	def leerPrograma(self):

		if self.__filename != None:

			print(self.__filename)
			print(self.obtenerToken("si"))
			#try:

			#	with open(self.__filename, "r") as archivo:

			#		for linea in archivo:
			#			print(linea)
			#			print(obtenerToken(linea))

			#except:
			#	print("Ha ocurrido un error en el proceso de lectura del programa eBlack")

eBlack = lexer_eBlack("Dictionary_eBlack.eb", "prueba.eb", None)
eBlack.leerPrograma()

#abrirArch_eBlack("Dictionary_eBlack.eb")
