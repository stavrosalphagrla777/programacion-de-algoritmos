import random
alumnos = []
def grabar_alumno():
    rut = input("ingrese el rut del alumno (8 digitos seguidos de un guion y una letra k o numero): ")
    nombre = input("ingrese el nombre del alumno (entre 2 y 12 caracteres): ")
    apellido = input ("ingrese el apellido del alumno: ")
    fecha_nacimiento = input("ingrese la fecha de nacimiento del alumno: ")
    carrera = input ("ingrese la carrera del alumno (enfermeria o contabilidad):")
    asignaturas = []
    while True:
        asignatura_nombre=input("ingrese el nombre de una asignatura (o exit para terminar): ")
        if asignatura_nombre == exit:
            break
        while True:
            
            promedio_str= input(f"ingrese el promedio de {asignatura_nombre}:")
            try:
                promedio = float(promedio_str)
                if promedio < 1.0 or promedio > 7.0:
                    print("el promedio debe estar entre 1.0 y 7.0.")
                else:
                    asignaturas.append((asignatura_nombre, promedio))
                    break
            except ValueError:
                print("el promedio debe ser un numero valido.")
            alumno = {rut,nombre,apellido,fecha_nacimiento,carrera,asignaturas}
            alumnos.append(alumno)
            print("alumno registrado exitosamente.")
            def buscar_alumno():
                rut_buscar = input("ingrese el rut del alumno a buscar.")
                for alumno in alumnos:
                    if alumno[rut] == rut_buscar:
                        print("informacion del alumno:")
                        print(f"rut:{alumno[rut]}")
                        print(f"nombre:{alumno[nombre]}")
                        print(f"apellido:{alumno[apellido]}")
                        print(f"fecha de nacimiento:{alumno[fecha_nacimiento]}")
                        print(f"carrera:{alumno[carrera]}")
                        if alumno[asignaturas]:
                            print("asignaturas y promedios:")
                            for asignatura in alumno[asignaturas]:
                                print(f"{asignatura[0]}:{asignatura[1]}")
                                return
                            print("alumno no encontrado.")
                            def imprimir_certificados():
                                for alumno in alumnos:
                                    certificado= random.randint(1000,5000)
                                    print("certificado de alumno regular:")
                                    print(f"nombre del certificado: alumno regular")
                                    print(f"rut del alumno: {alumno[rut]}")
                                    print(f"nombre:{alumno[nombre]} {alumno[apellido]}")
                                    print(f"carrera:{alumno[carrera]}")
                                    if alumno[asignaturas]:
                                        print("asignaturas y promedios:")
                                        for asignatura in alumno[asignaturas]:
                                            print(f"{asignatura[0]} {asignatura[1]}")
                                            print("-------")
                                            print("certificado de la matricula:")
                                            print(f"nombre del certificado:matricula")
                                            print(f"rut del alumno:{alumno[rut]}")
                                            print(f"nombre:{alumno[nombre]}{alumno[apellido]}")
                                            print(f"carrera:{alumno[carrera]}")
                                            print(f"monto:${certificado}")
                                            print("----------------------")
                                            while True:
                                                print("menu:")
                                                print("1.grabar alumno")
                                                print("2.buscar alumno")
                                                print("3.imprimir certificados")
                                                print("4.salir")
                                                opcion =input("ingrese su opcion:  ")
                                                if opcion == 1:
                                                    grabar_alumno()
                                                elif opcion == 2:
                                                    buscar_alumno()
                                                elif opcion == 3:
                                                    imprimir_certificados()
                                                elif opcion == 4:
                                                    print("!hasta luego!")
                                                    break
                                                else:
                                                    print("opcion invalida. intente nuevamente.")

grabar_alumno()



                    



            
            