import os # Rutas y archivos
import re # Regular expression

"""
Busca un patron en todos los archivos de texto dentro de un directorio
y guarda las lineas coincidentes en un archivo de resultados.

Parametros:
- directorio: la ruta del directorio donde buscar.
- patron: el patron a buscar (expresion regular).
- archivo_resultado: archivo donde se guardaran las coincidencias.
"""
def buscar_patron_en_archivos(directorio, patron, archivo_resultado):
    # Compilar el patron para hacer la busqueda mas eficiente
    regex = re.compile(patron)
    
    # Abrir archivo donde se guardan los resultados de la busqueda
    with open(archivo_resultado, 'w') as resultado:

        # Recorrer todos los archivos en el directorio
        for archivo in os.listdir(directorio):

            ruta_archivo = os.path.join(directorio, archivo)
            
            # Solo buscar en archivos de texto
            if os.path.isfile(ruta_archivo) and archivo.endswith('.txt'):
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                
                # Buscar el patron en cada linea
                for num_linea, linea in enumerate(lineas, 1):
                    if regex.search(linea):
                        # Escribir la linea coincidente en el archivo de resultados
                        resultado.write(f"Archivo: {archivo}, Línea {num_linea}: {linea}")

    print(f"Resultados guardados en {archivo_resultado}")

# Parametros para la busqueda
directorio_a_buscar = 'directorioPalabras'
# patron_a_buscar = r'patron'

patron_a_buscar = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# patron_a_buscar = r'\b\d{4}-\d{2}-\d{2}\b'
# patron_a_buscar = r'\b(?:\d{1,3}\.){3}\d{1,3}\b' # 123.89.46.72 
# patron_a_buscar = r'https?://[^\s]+'
# patron_a_buscar = r'\bpalabra\b'
# patron_a_buscar = r'^palabra'
# patron_a_buscar = r'palabra$'

archivo_salida = 'resultados_busqueda.txt'

# Llamada a la funcion para buscar el patron
buscar_patron_en_archivos(directorio_a_buscar, patron_a_buscar, archivo_salida)
