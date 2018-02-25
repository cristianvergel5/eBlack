def leer_eBlack(name):

	if name.find(".eb") == False:
		name = name + ".eb"

	try:

		with open(name, "r") as archivo:
			for line in archivo:
				print(line)

	except:
		print("No existe un archivo eBlack con ese nombre, asegurese de que tenga extension .eb")

def obtenerToken(simbolo):

	simbolo = simbolo.lower() +  "\n"
	tipo = ""

	try:

		with open("Dictionary_eBlack.eb", "r") as diccionario:
			
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
				
#abrirArch_eBlack("Dictionary_eBlack.eb")
