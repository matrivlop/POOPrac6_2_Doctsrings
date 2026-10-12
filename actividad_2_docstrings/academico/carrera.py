"""Define Carrera para agrupar las materias de un programa universitario."""


class Carrera:
  """Representa una carrera y permite agregar materias a su plan.

  Attributes:
      nombreC (str): Nombre de la carrera.
      claveC (str): Clave de la carrera.
      lisMateria (list[Materia]): Materias agregadas a la carrera.
  """

  def __init__(self, nombreC, claveC,):
    """Inicializa una carrera con una lista de materias vacia.

    Args:
        nombreC (str): Nombre de la carrera.
        claveC (str): Clave que identifica la carrera.

    Returns:
        None.
    """
    self.nombreC = nombreC
    self.claveC = claveC
    self.lisMateria = []

  def agregar_materia(self, materia):
        """Agrega una materia a la lista e imprime una confirmacion.

        Args:
            materia (Materia): Materia que se agrega, sin validar duplicados.

        Returns:
            None.
        """
        self.lisMateria.append(materia)
        print("Materia agregada exitosamente a la carrera {}".format(self.nombreC))
