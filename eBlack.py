import win32com.client as clwin
import re

operadores = {'SUMA':'+', 'RESTA':'-', 'MULTIPLICACION':'*', 'DIVISION': '/', 'ASIGNACION': '~', 'MENOR QUE': '<',
'MAYOR QUE':'>', 'IGUAL':'~~', 'MENOR IGUAL':'<~', 'MAYOR IGUAL':'>~', 'DIFERENTE':'|~'}

tokens = ['ID', 'NUMERO', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'PARENTESISI', 'PARENTESISD']

puntuacion = {'PUNTO':'.', 'COMA':',', 'PUNTO Y COMA':';', 'DOS PUNTOS': ':', 'PUNTOS SUSPENSIVOS':'...',
'PARENTESIS IZQUIERDO':'(', 'PARENTESIS DERECHO':')', 'CORCHETE IZQUIERDO':'[', 'CORCHETE DERECHO':']', 'BARRA':'',
'LLAVE IZQUIERDA':'{', 'LLAVE DERECHA':'}'}

reservadas = ['itr', 'miq', 'si', 'sino', 'entonces', 'retorna', 'clase', 'prueba', 'ajuste', 'verdad', 'falso', 'casos']

def SapiLee(lectura):
	habla = clwin.Dispatch("SAPI.SpVoice")
	habla.Speak(lectura)

def identificarID(identificar):
	patron = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')

	identificar = identificar.lower()
	
	if identificar not in operadores.values() and identificar not in reservadas and patron.search(identificar) != None:
		return "[ID, "+identificar+"]"

	return False

def identificarNUM(identificar):
	
	patron = re.compile(r'\d+')

	if patron.search(identificar) != None:
		return True

	return False

def identificarComentario(identificar):

	patron = re.compile(r'\|.*')

	if patron.search(identificar) != None:
		return True

	return False
	
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

	@dictionary.deleter
	def dictionary(self):
		self.__dictionary = None

	@property
	def filename(self):
		return self.__dictionary

	@filename.setter
	def filename(self, filename):
		self.__filename = filename

	@filename.deleter
	def filename(self):
		self.__filename = None

	@property
	def tokens(self):
		return self.__tokens

	@tokens.setter
	def tokens(self, token):
		self.__tokens.append(token)

	@tokens.deleter
	def tokens(self):
		self.__tokens = None

	def obtenerToken(self, simbolo):

		simbolo = simbolo.lower()
		simbolo = simbolo.rstrip("\n")
		parecido = ""
		tipo = ""

		try:

			if simbolo in reservadas:
				return "["+"PALABRA RESERVADA, "+simbolo+"]"
			elif simbolo in operadores.values():
				return "["+"OPERADOR, "+simbolo+"]"
			
			return None

		except:
			print("Ha ocurrido un error")


	def leerPrograma(self):

		if self.__filename != None:

			contador = 1
			lista = []

			try:

				with open(self.__filename, "r") as archivo:

					for linea in archivo:
						
						lista = linea.split(" ")

						for i in lista:

							valor = self.obtenerToken(i)

							if valor == None:
								self.tokens = "Error en la linea " + str(contador)
								#return activar el return para salir del programa cuando encuentre un error
							else:
								self.tokens = str(valor) + ". Linea: " + str(contador)

						contador = contador + 1

			except:
				print("Ha ocurrido un error en el proceso de lectura del programa eBlack")

"""
SapiLee("Inicio de lexer eBlack")
eBlack = lexer_eBlack("Dictionary_eBlack.eb", "prueba.eb")
eBlack.leerPrograma()
Resultado = eBlack.tokens
for i in Resultado:
	print(i)
	SapiLee(i)

print(identificarID("si"))
SapiLee("Fin de lexer eBlack")
#abrirArch_eBlack("Dictionary_eBlack.eb")
"""

def separarExpresion(linea, lista, n):

	#print("INICIO: ", linea)

	#print("LISTA SUCESION N->", n)
	for i in lista:
		print(i)
	
	if "=" not in linea:
		lista.append(linea)

	elif "=" in linea:
		
		palabra = linea[n:linea.index("=")]
		n = linea.index("=")
		#print("EXTRAIDA: ", palabra, " N ->", n)
		lista.append(palabra)

		if "=" not in lista:
			lista.append("=")

		#print("SIGUIENTE SUCESION: ", linea[linea.index("=")+1:], "\n\n")
		separarExpresion(linea[linea.index("=")+1:], lista, 0)
	
	return lista
