def abrirArch_eBlack(name):

	if name.find(".eb") == False:
		name = name + ".eb"

	try:

		with open(name, "r") as archivo:
			for line in archivo:
				print(line)

	except:
		print("No existe un archivo eBlack con ese nombre, asegurese de que tenga extension .eb")

abrirArch_eBlack("prueba.eb")
