def print_args(args):
   modulos.validate_args(args)
   directory1 = args.dir1
   directory2 = args.dir2
   salida= args.output
   print(f'Directorio 1: {directory1}  Directorio 2: {directory2}  salida {salida}')



-----------------


def validar(self):
   respuesta = True
   self.argumentos = self.opciones.parse_args()

   respuesta = (self.argumentos.modificaton_date or self.argumentos.size or self.argumentos.fingerprint) \
               and validaciones.esdirectorio(self.argumentos.dir1) \
               and validaciones.esdirectorio(self.argumentos.dir2) \
               and validaciones.directorio_existe(self.argumentos.output) \
               and validaciones.directorios_iguales(self.argumentos.dir1, self.argumentos.dir2)

   return respuesta

   # function to print both directories


def print_args(self):
   if self.validar():
      directory1 = self.argumentos.dir1
      directory2 = self.argumentos.dir2
      salida = self.argumentos.output
      print(f'Directorio 1: {directory1}  Directorio 2: {directory2}  salida {salida}')
   else:
      print("self.validar()")