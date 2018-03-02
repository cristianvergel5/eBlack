import win32com.client as clwin
import re

operadores = {'SUMA':'+', 'RESTA':'-', 'MULTIPLICACION':'*', 'DIVISION': '/', 'ASIGNACION': '~', 'MENOR QUE': '<',
'MAYOR QUE':'>', 'IGUAL':'~~', 'MENOR IGUAL':'<~', 'MAYOR IGUAL':'>~', 'DIFERENTE':'|~', 'MODULO':'%',
'LLAVE IZQUIERDA':'{', 'LLAVE DERECHA':'}', 'COMA':',', 'PARENTESIS IZQUIERDO':'(', 'PARENTESIS DERECHO':')'}

tokens = ['ID', 'NUMERO', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'PARENTESISI', 'PARENTESISD']

puntuacion = {'PUNTO':'.', 'COMA':',', 'PUNTO Y COMA':';', 'DOS PUNTOS': ':', 'PUNTOS SUSPENSIVOS':'...', 'CORCHETE IZQUIERDO':'[', 'CORCHETE DERECHO':']'}

reservadas = ['itr', 'miq', 'si', 'sino', 'entonces', 'retorna', 'clase', 'prueba', 'ajuste', 'verdad', 'falso', 'casos', 'escriba',
'funcion']

def SapiLee(lectura):
	habla = clwin.Dispatch("SAPI.SpVoice")
	habla.Speak(lectura)

def identificarReservada(identificar):
	

def identificarID(identificar):
	patron = re.compile(r'[&][a-zA-Z_][a-zA-Z0-9_]*')

	identificar = identificar.lower()
	
	if identificar not in operadores.values() and identificar not in reservadas and patron.search(identificar) != None:
		return "[IDENTIFICADOR, "+identificar+" ]"

	return False

def identificarComentario(identificar):

	patron = re.compile(r'\|.*')

	if patron.search(identificar) != None:
		return True

	return False

def identificarString(identificar):
	patron = re.compile(r'\".*\"')

	if patron.search(identificar) != None:
		return True

	return False

def identificarNumero(identificar):

	flotante = identificar
	flotante = flotante.replace(",", "")
	flotante = flotante.replace(".", "")

	if identificar.isdigit() == True:
		return "[ENTERO, "+identificar+" ]"
	elif flotante.isdigit() == True:
		return "[FLOTANTE, "+identificar+" ]"

	return False
	
class lexer_eBlack():

	def __init__(self, filename):
		self.__filename = filename
		self.__tokens = []

	@property
	def filename(self):
		return self.__filename

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
		simbolo = simbolo.rstrip("\t")
		simbolo = simbolo.replace(" ", "")
		parecido = ""
		tipo = ""

		try:

			if simbolo in reservadas:
				return "["+"PALABRA RESERVADA, "+simbolo+" ]"
			elif simbolo in operadores.values():
				return "["+"OPERADOR, "+simbolo+" ]"
			elif identificarID(simbolo) != False:
				return identificarID(simbolo)
			elif identificarNumero(simbolo) != False:
				return identificarNumero(simbolo)

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

							if identificarComentario(i) != True:

								valor = self.obtenerToken(i)

								if valor == None:
									self.tokens = "Error en la linea " + str(contador)
									#return activar el return para salir del programa cuando encuentre un error
								else:
									self.tokens = str(valor) + ". Linea: " + str(contador)
							else:
								break;

						contador = contador + 1

			except:
				print("Ha ocurrido un error en el proceso de lectura del programa eBlack")

print(identificarString("Cadena de caracteres"))

SapiLee("Inicio de lexer eBlack")
eBlack = lexer_eBlack("prueba.eb")
eBlack.leerPrograma()
Resultado = eBlack.tokens

for i in Resultado:
	print(i)
#	SapiLee(i)

SapiLee("Fin de lexer eBlack")
#abrirArch_eBlack("Dictionary_eBlack.eb")


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
