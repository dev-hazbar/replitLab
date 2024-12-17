import os

'''Obtener el directorio actual'''
directorio_actual = os.getcwd()

'''Ruta al archivo que deseas ejecutar'''
# ruta_archivo = "./dataRead/readToml.py"
# ruta_archivo = "./dataRead/readHcl.py"
# ruta_archivo = "./dataRead/readJson.py"
# ruta_archivo = "./dataRead/readIni.py"
# ruta_archivo = "./dataRead/readXml.py"
# ruta_archivo = "./dataRead/readCsv.py"

#ruta_archivo = "./cpDataRead/cpDataGeneral/inputReader.py"

ruta_archivo = "./mathCP/001_numberTheory/001_modAritmetic/02_problemas/001_modulo/get_mod.py"
ruta_archivo = "./mathCP/001_numberTheory/001_modAritmetic/02_problemas/002_find_last_digit_of_power/find_last_dist_power.py"

#ruta_archivo = "./importOutFiles/testSource/elorion.py"
#ruta_archivo = "./mathCP/modAritmetic/get_mod/get_mod.py"
#ruta_archivo = "./mathCP/modAritmetic/mod_exp/mod_exp.py"
#ruta_archivo = "./mathCP/modAritmetic/mod_exp/mod_exp_mulIt.py"
#ruta_archivo = "./mathCP/modAritmetic/mod_exp/mod_exp_by_fastexp.py"
#ruta_archivo = "./mathCP/modAritmetic/mod_inverse/mod_inverse.py"

try:
    # Cambiar al directorio del archivo
    os.chdir(os.path.dirname(ruta_archivo))

    # Ahora estás en el directorio del archivo, puedes ejecutarlo
    os.system("python " + os.path.basename(ruta_archivo))

#except Exception as e:
#    print("Ocurrió un error:")


finally:
    # Volver al directorio original al finalizar
    os.chdir(directorio_actual)
