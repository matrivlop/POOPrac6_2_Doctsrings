"""Define Alumno para consultar datos, derecho a examen y promedio."""


class Alumno:
  """Representa un alumno con asistencias, materias y calificaciones.

  Permite mostrar sus datos, evaluar el derecho a examen, registrar
  calificaciones y mostrar el promedio.

  Attributes:
      nombre (str): Nombre del alumno.
      numCuenta (str): Numero de cuenta del alumno.
      carrera (str): Carrera que cursa.
      semestre (int): Semestre actual.
      numAsistencia (int): Dias de asistencia sobre 100 dias de clase.
      numInscritas (int): Numero de materias inscritas.
      listaCalif (list[float]): Calificaciones; existe solo despues de
          una llamada exitosa a ingresarCalif(). Tambien admite enteros.
  """

  def __init__(self, nombre, numCuenta, carerra, semestre, numAsistencia, numInscritas):
    """Inicializa los datos escolares del alumno.

    Args:
        nombre (str): Nombre del alumno.
        numCuenta (str): Numero de cuenta del alumno.
        carerra (str): Nombre de la carrera; se guarda en self.carrera.
        semestre (int): Semestre que cursa.
        numAsistencia (int): Cantidad de dias asistidos.
        numInscritas (int): Cantidad de materias inscritas.

    Returns:
        None.
    """
    self.nombre = nombre
    self.numCuenta = numCuenta
    self.carrera = carerra
    self.semestre = semestre
    self.numAsistencia = numAsistencia
    self.numInscritas = numInscritas

  def mostrar(self):
    """Imprime los datos personales y escolares del alumno.

    Returns:
        None.
    """
    print("Nombre Alumno : {}".format(self.nombre))
    print("Numero de Cuenta : {}".format(self.numCuenta))
    print("Carrera : {}".format(self.carrera))
    print("Semestre : {}".format(self.semestre))
    print("Numero de Asistencia : {}".format(self.numAsistencia))
    print("Numero de Materias Inscritas : {}".format(self.numInscritas))

#Vamos a homogeneizar el sistema para facilitar su calculo a atravez de las siguientes reglas. 
#1.- El semestre dura 5 meses de clases, el otro es de vacaciones, cada mes tiene exactamente 28 dias
#es decir, 4 semenas exactas, por ende, son 140 dias, pero, justamente 40 dias son de fin de semana
#vamos a suponer que no hay clases sabatinas, asi pues, solo evaluamos 100 dias exactos.
#2.- Si el individuo registra asistencia, vamos a asumir que hizo todos sus deberes, si tenia 3 clases 
#un dia y tuvo asistencia, entro a esas 3 clases. 
#3.- Cada clase dura 2 horas, el calculo de creditos por materia, es el numero de horas que se le tiene 
#que dedicar por semana, por ejemplo, si una materia tiene 8 creditos, implica que a la semana se
#impartieron 4 clases. 

  def derechoExamen(self):
    """Determina e imprime si el alumno tiene derecho a examen.

    Usa un minimo de 80 asistencias sobre un semestre de 100 dias.

    Returns:
        bool: True si numAsistencia es al menos 80; False en otro caso.
    """
    asistencia = self.numAsistencia
    if asistencia >= 80 :
      print("El alumno {} tiene derecho a examen en sus materias".format(self.nombre))
      return True
    else:
      print("El alumno {} NO tiene derecho a examen en sus materias".format(self.nombre))
      return False

#Añadir el :list, fue ayuda de IA para dar indicaciones
  def ingresarCalif(self, listaCalif: list):
    """Guarda las calificaciones si su cantidad coincide con las materias.

    Conserva la misma lista recibida, sin copiarla. Solo comprueba su
    longitud; no valida el tipo ni el rango de las calificaciones.

    Args:
        listaCalif (list[float]): Una calificacion por materia inscrita;
            tambien admite valores enteros para calcular el promedio.

    Returns:
        bool: True si guarda la lista; False si la cantidad no coincide.
        En caso de False, conserva cualquier lista guardada previamente.
    """
    if len(listaCalif) == self.numInscritas:
      self.listaCalif = listaCalif
      return True
    else: 
      return False

  def calcularProm(self, listaCalif: list):
    """Registra las calificaciones y muestra su promedio aritmetico.

    Llama a ingresarCalif(). Si la cantidad no coincide con numInscritas,
    imprime un aviso. Para calcular, la lista debe ser numerica y no vacia.

    Args:
        listaCalif (list[float]): Calificaciones de las materias inscritas;
            tambien admite valores enteros.

    Returns:
        None: El promedio se imprime, no se devuelve.

    Raises:
        ZeroDivisionError: Si numInscritas es cero y la lista esta vacia.
        TypeError: Si la lista aceptada contiene valores no sumables
            con numeros.
    """
    if self.ingresarCalif(listaCalif)==True:
      sum = 0
      for i in self.listaCalif:
        sum = sum + i
      prom = sum/len(self.listaCalif)
      print("El promedio final del alumno {} es de {}".format(self.nombre, prom))
    else:
      print("No se pudo calcular el promedio de forma exitosa")
