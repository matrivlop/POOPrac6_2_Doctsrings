"""Define Empleado y el calculo de su sueldo con horas extra al doble."""


class Empleado:
  """Representa un empleado y permite mostrar su sueldo calculado.

  Attributes:
      nombreE (str): Nombre del empleado.
      numCuentaE (str): Numero de cuenta del empleado.
      puesto (str): Puesto desempenado.
      sueldoE (float): Pago por hora ordinaria.
      horasTrabajadas (int): Horas ordinarias trabajadas en el semestre.
      horasExtra (int): Horas extra trabajadas en el semestre.
  """

  def __init__(self, nombreE, numCuentaE, puesto, sueldoE, horasTrabajadas, horasExtra):
    """Inicializa los datos laborales del empleado.

    Args:
        nombreE (str): Nombre del empleado.
        numCuentaE (str): Numero de cuenta del empleado.
        puesto (str): Puesto que ocupa.
        sueldoE (float): Pago por hora ordinaria; tambien admite enteros.
        horasTrabajadas (int): Horas ordinarias del semestre.
        horasExtra (int): Horas extra del semestre, pagadas al doble.

    Returns:
        None.
    """
    self.nombreE = nombreE
    self.numCuentaE = numCuentaE
    self.puesto = puesto
    self.sueldoE = sueldoE
    self.horasTrabajadas = horasTrabajadas
    self.horasExtra = horasExtra

#De igual forma se va a considerar el sistema completamente homogeneo.
#Como en este caso, no son profesores y pueden ser directivos y pueden tener mas o menos horas
# en fines de semana o entre semana, las horas extra y demas, este se calculo directo, peroooo
# las horas extras las vamos a pagar al doble, solo para ver como funciona. 
# si hay 140 dias, de los cuales, digamos que si solo duermen, comen (1 horas por comida) y trabajan
# (2 horas en llegar al trabajo), el maximo de horas que pueden trabajar por dia es de 11 horas.
# si hay 140 dias, como maximo, pueden trabajar 1540 horas, ahora, la jornada laboral es de 8 horas,
# es decir, 1120 horas se puede trabajar el jornada laboral, 420 como horas extra. 

  def calculoSueldoE(self):
    """Calcula e imprime el sueldo semestral, mensual y semanal.

    Acepta de 0 a 1120 horas ordinarias y de 0 a 420 horas extra.
    Si las horas quedan fuera de esos limites, imprime un aviso.
    El total suma horas ordinarias por sueldoE y horas extra por el
    doble de sueldoE. Divide entre 5 meses y luego entre 4 semanas.

    Returns:
        None: Los importes se imprimen, no se devuelven.
    """
    if self.horasTrabajadas<0 :
      print("No puedes trabajar horas negativas")
    elif self.horasExtra<0: 
      print("No puedes trabajar horas negativas")
    elif self.horasTrabajadas > 1120:
      print("No puedes trabajar mas horas de las posibles")
    elif self.horasExtra > 420:
      print("No puedes trabajar mas horas de las posibles")
    else:
      sueldoSemeE = (self.horasTrabajadas * self.sueldoE) + (self.horasExtra * 2 * self.sueldoE)
      sueldoMesE = sueldoSemeE/5
      sueldoSemaE = sueldoMesE/4
      print("El empleado {} con puesto {}, gano {} en todo el semestre".format(self.nombreE , self.puesto, sueldoSemeE))
      print("es decir gano {} por mes".format(sueldoMesE))
      print("es decir gano {} por semana".format(sueldoSemaE))
