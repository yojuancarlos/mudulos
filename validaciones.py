import os

def existe_ruta(directory):
    return  os.path.exists(directory)

def esdirectorio(directory):
#si es directorio me retorna true sino lo es retorna false
    return os.path.isdir(directory)

def esarchivo(directory):
# si es archivo me retorna true sino lo es retorna false
    return os.path.isfile(directory)
