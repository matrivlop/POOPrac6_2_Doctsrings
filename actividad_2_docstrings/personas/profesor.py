"""Define Profesor para consultar sus datos y calcular su sueldo."""


class Profesor:
  """Representa un profesor y permite mostrar sus datos y sueldo.

  Attributes:
      nombreP (str): Nombre del profesor.
      numCuentaP (str): Numero de cuenta del profesor.
      departamento (str): Departamento al que pertenece.
      sueldoP (float): Pago por hora.
      numAsistenciaP (int): Dias asistidos durante el semestre.
      numHoras (int): Horas por dia usadas en el calculo del sueldo.
  """

  def __init__(self, nombreP, numCuentaP, departamento, sueldoP, numAsistenciaP, numHoras):
    """Inicializa los datos laborales del profesor.

    Args:
        nombreP (str): Nombre del profesor.
        numCuentaP (str): Numero de cuenta del profesor.
        departamento (str): Departamento de adscripcion.
        sueldoP (float): Pago por hora; tambien admite enteros.
        numAsistenciaP (int): Cantidad de dias asistidos.
        numHoras (int): Horas de trabajo por dia segun el modelo original.

    Returns:
        None.
    """
    self.nombreP = nombreP
    self.numCuentaP = numCuentaP
    self.departamento = departamento
    self.sueldoP = sueldoP
    self.numAsistenciaP = numAsistenciaP
    self.numHoras = numHoras

  def mostrarP(self):
    """Imprime los datos personales y laborales del profesor.

    Returns:
        None.
    """
    print("Nombre Profesor : {}".format(self.nombreP))
    print("Numero de Cuenta : {}".format(self.numCuentaP))
    print("Departamento : {}".format(self.departamento))
    print("Sueldo : {}".format(self.sueldoP))
    print("Numero de Asistencia : {}".format(self.numAsistenciaP))
    print("Numero de Horas : {}".format(self.numHoras))

#De igual forma se va a considerar el sistema completamente homogeneo.
#Ya paso el semestre, si se asisten un dia, se asistenten a todas las clases o jornada laboral
# 100 dias de trabajo realmente, vamos a considerar que los fines de semana tampoco trabajan
# el sueldo es lo que le pagan por hora y el numero de horas, son las horas que le dieron por dia. 

  def calculoSueldoP(self):
    """Calcula e imprime el sueldo semestral, mensual y semanal.

    Acepta de 0 a 100 dias de asistencia; fuera del intervalo imprime
    un aviso. Multiplica numHoras por numAsistenciaP y por sueldoP.
    Divide el total entre 5 meses y el sueldo mensual entre 4 semanas.

    Returns:
        None: Los importes se imprimen, no se devuelven.
    """
    if self.numAsistenciaP<0:
      print("No puedes tener asistencia negativa")
    elif self.numAsistenciaP>100:
      print("No puedes tener mas asistencia de la que hubo")
    else:
      sueldoSeme = self.numHoras * self.numAsistenciaP * self.sueldoP
      sueldoMes = sueldoSeme/5
      sueldoSema = sueldoMes/4
      print("El profesor {}, gano {} en todo el semestre".format(self.nombreP ,sueldoSeme))
      print("es decir gano {} por mes".format(sueldoMes))
      print("es decir gano {} por semana".format(sueldoSema))
