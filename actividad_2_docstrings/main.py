"""Ejecuta una demostracion del sistema de administracion universitaria.

Incluye main() y mostrar_resumen_general(). Usa datos de ejemplo y requiere
elegir una accion desde la terminal:

    python main.py --accion resumen

Acciones: resumen, alumnos, derecho_examen, sueldo_emp, promedio y usuarios.
"""

import argparse
from personas.alumno import Alumno
from personas.profesor import Profesor
from academico.materia import Materia
from academico.carrera import Carrera
from administrativo.empleado import Empleado
from usuario.usuarios import Usuarios

def mostrar_resumen_general(lista_alumnos, lista_profesores, lista_materias, lista_carreras):
    """Imprime las cantidades de registros de la universidad.

    Args:
        lista_alumnos (list[Alumno]): Alumnos que se contabilizan.
        lista_profesores (list[Profesor]): Profesores que se contabilizan.
        lista_materias (list[Materia]): Materias que se contabilizan.
        lista_carreras (list[Carrera]): Carreras que se contabilizan.

    Returns:
        None.
    """
    print("\n--- RESUMEN GENERAL DE LA UNIVERSIDAD ---")
    print("Total de Alumnos matriculados: {}".format(len(lista_alumnos)))
    print("Total de Profesores activos: {}".format(len(lista_profesores)))
    print("Total de Materias impartidas: {}".format(len(lista_materias)))
    print("Total de Carreras disponibles: {}".format(len(lista_carreras)))
    print("-----------------------------------------\n")

def main():
    """Crea los datos de ejemplo y ejecuta la accion de la terminal.

    Configura profesores, materias, una carrera y registros de alumnos
    antes de interpretar --accion; esa preparacion imprime mensajes.

    Returns:
        None.

    Raises:
        SystemExit: Cuando argparse muestra la ayuda o recibe argumentos
            ausentes o invalidos.
    """
    alu1 = Alumno("Jorge", "1637821", "Telecomunicaciones", 6, 85, 3)
    alu2 = Alumno("Ana", "1234567", "Telecomunicaciones", 4, 75, 4)
    
    prof1 = Profesor("Ing. Lopez", "5432", "Sistemas", 150, 100, 40)
    prof2 = Profesor("Dr. Martinez", "9876", "Fisica", 200, 95, 30)
    
    emp1 = Empleado("Don Ramon", "1111", "Mantenimiento", 50, 1000, 50)
    
    mat1 = Materia("Programacion", "0432", 8)
    mat2 = Materia("Fisica Cuantica", "0101", 8)
    

    car1 = Carrera("Ingenieria en Telecomunicaciones", "0011")
    
    usu1 = Usuarios("jorge_tel", "password123", "Alumno")
    usu2 = Usuarios("admin_ramon", "secreto", "Empleado")

    mat1.agregar_profesor(prof1)
    mat2.agregar_profesor(prof2)
    car1.agregar_materia(mat1)
    car1.agregar_materia(mat2)
    
    mat1.registrarAlumno() 
    mat1.registrarAlumno()

    todos_alumnos = [alu1, alu2]
    todos_profesores = [prof1, prof2]
    todas_materias = [mat1, mat2]
    todas_carreras = [car1]

#********En general la IA me ayudo a hacer la parte del main, pero fueron cosas simples********
#En argparser, fue donde realmente no entendi bien que hacer y fue donde mas se uso la IA
    parser = argparse.ArgumentParser(description="Sistema de Administracion Universitaria")
    
    parser.add_argument("--accion", 
        choices=["resumen", "alumnos", "derecho_examen", "sueldo_emp", "promedio", "usuarios"],
        help="Que accion deseas ejecutar en el sistema?", 
        required=True)
    
    args = parser.parse_args()

    if args.accion == "resumen":
        mostrar_resumen_general(todos_alumnos, todos_profesores, todas_materias, todas_carreras)    
    elif args.accion == "alumnos":
        print("\n--- INFO DE ALUMNOS ---")
        alu1.mostrar()
        print("")
        alu2.mostrar()    
    elif args.accion == "derecho_examen":
        print("\n--- VERIFICACION DE DERECHO A EXAMEN ---")
        alu1.derechoExamen()
        alu2.derechoExamen()    
    elif args.accion == "sueldo_emp":
        print("\n--- CALCULO DE NOMINA ---")
        emp1.calculoSueldoE()
        prof1.calculoSueldoP()
    elif args.accion == "promedio":
        print("\n--- CALCULO DE PROMEDIOS ---")
        alu1.calcularProm([80, 90, 100])  
    elif args.accion == "usuarios":
        print("\n--- VERIFICACION DE USUARIOS ---")
        usu1.determinarUsuario()
        usu2.determinarUsuario()

if __name__ == "__main__":
    main()
