"""Define Usuarios para almacenar una cuenta y mostrar su tipo."""


class Usuarios:
  """Representa una cuenta de alumno, profesor o empleado.

  Permite mostrar el tipo asignado mediante determinarUsuario().

  Attributes:
      nombreU (str): Nombre de la cuenta.
      contrasena (str): Contrasena guardada tal como se recibe.
      tipoUsuario (str): Alumno, Profesor, Empleado o Desconocido.
  """

  def __init__(self, nombreU, contrasena, tipoUsuario):
    """Inicializa una cuenta y comprueba el nombre de su tipo.

    Args:
        nombreU (str): Nombre de usuario.
        contrasena (str): Contrasena de la cuenta.
        tipoUsuario (str): Alumno, Profesor o Empleado, respetando
            mayusculas. Otro valor se sustituye por Desconocido y
            provoca que se imprima una advertencia.

    Returns:
        None.
    """
    self.nombreU = nombreU
    self.contrasena = contrasena

    posiblesUsua = ["Alumno", "Profesor", "Empleado"]
    if tipoUsuario in posiblesUsua:
      self.tipoUsuario = tipoUsuario
    else:
      self.tipoUsuario = "Desconocido"
      print("Advertencia: Usuario no valido en la universidad {}".format(self.nombreU))

#En esta parte no supe como pedirlo, pense en crear una lista con 3 nombres, alumno, profesor, empleado,
# que cada cuenta tenga una estructura, por ejemplo, que todos los alumnos empiezen por 1 en su cuenta
# o que los alumnos, su cuenta sea modulo de 2, pero la verdad no supe como implementar esto

  def determinarUsuario(self):
    """Imprime el nombre de la cuenta y su tipo de usuario.

    Returns:
        None: El tipo se imprime, no se devuelve.
    """
    print("El usuario {} es un {} de la universidad".format(self.nombreU, self.tipoUsuario))


  

