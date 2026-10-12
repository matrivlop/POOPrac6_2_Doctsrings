"""Demuestra consultas de docstrings del proyecto con __doc__ y help().

Uso desde la carpeta del proyecto:
    python consultar_documentacion.py
"""

from personas.alumno import Alumno


def main():
    """Muestra la documentacion de Alumno y de algunos de sus metodos.

    Returns:
        None.
    """
    print("--- Docstring de la clase Alumno ---")
    print(Alumno.__doc__)
    print("\n--- Docstring del metodo ingresarCalif ---")
    print(Alumno.ingresarCalif.__doc__)
    print("\n--- Ayuda del metodo derechoExamen ---")
    help(Alumno.derechoExamen)


if __name__ == "__main__":
    main()
