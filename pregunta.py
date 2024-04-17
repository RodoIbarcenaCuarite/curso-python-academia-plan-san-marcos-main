def registrar_empleado(registro_empleados):
    while True:
        id_empleado = input("Ingrese el ID del empleado: ")
        if id_empleado in registro_empleados:
            print("Este ID ya existe. Intente con otro.")
            continue
        nombre = input("Ingrese el nombre completo del empleado: ")
        dni = input("Ingrese el DNI del empleado: ")
        telefono = input("Ingrese el teléfono del empleado: ")
        tiempo_trabajando = input("Ingrese el tiempo trabajando del empleado (meses): ")
        cargo = input("Ingrese el cargo del empleado: ")

        salario = obtener_salario_segun_cargo(cargo)

        registro_empleados[id_empleado] = {
            'nombre': nombre,
            'dni': dni,
            'telefono': telefono,
            'tiempo_trabajando': tiempo_trabajando,
            'cargo': cargo,
            'salario': salario
        }

        respuesta = input("¿Quiere ingresar un nuevo empleado al registro? (Si/ No): ")
        if respuesta.lower() != 'si':
            break

    return registro_empleados

def obtener_salario_segun_cargo(cargo):
    salarios = {
        'Limpieza': 1025.00,
        'Mesero': 1500.00,
        'Cajero': 1500.00,
        'Vigilante': 1400.00,
        'Gerente': 2500.00
    }
    return salarios.get(cargo, 0)

def visualizar_informacion_empleado(registro_empleados):
    id_empleado = input("Ingrese el ID del empleado a visualizar: ")
    empleado = registro_empleados.get(id_empleado)
    if empleado:
        print(f"Información del empleado con ID {id_empleado}: {empleado}")
    else:
        print("No se encontró un empleado con ese ID.")

def mostrar_empleado_menor_tiempo(registro_empleados):
    if registro_empleados:
        empleado_menor_tiempo = min(registro_empleados.values(), key=lambda x: x['tiempo_trabajando'])
        print(f"Empleado con menor tiempo en la empresa: {empleado_menor_tiempo}")
    else:
        print("No hay empleados registrados.")

def actualizar_salario_empleado(registro_empleados):
    id_empleado = input("Ingrese el ID del empleado a actualizar salario: ")
    if id_empleado in registro_empleados:
        nuevo_salario = float(input("Ingrese el nuevo salario: "))
        registro_empleados[id_empleado]['salario'] = nuevo_salario
        print("Salario actualizado correctamente.")
    else:
        print("No se encontró un empleado con ese ID.")


def visualizar_informacion_empleado(registro_empleados):
    try:
        print("========== Visualizar Información ==========")
        id_empleado = input("Ingrese el Id del empleado: ")
        if id_empleado in registro_empleados:
            empleado = registro_empleados[id_empleado]
            print(f"ID: {id_empleado}")
            for clave, valor in empleado.items():
                print(f"{clave.capitalize()}: {valor}")
        else:
            print("Lo sentimos, no se encontró un empleado con ese Id.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def mostrar_empleado_minimo_tiempo(registro_empleados):
    tiempos_trabajando = {id_empleado: int(info['tiempo_trabajando']) for id_empleado, info in registro_empleados.items()}
    
    menor_tiempo = min(tiempos_trabajando.values()) if tiempos_trabajando else None
    
    empleados_menor_tiempo = {id_empleado: info for id_empleado, info in registro_empleados.items() if int(info['tiempo_trabajando']) == menor_tiempo}
    
    if len(empleados_menor_tiempo) == 1:
        print("========== Empleado con menor tiempo en la empresa ==========")
        for id_empleado, info in empleados_menor_tiempo.items():
            print(f"Id: {id_empleado}")
            print(f"Nombre: {info['nombre']}")
            print(f"Tiempo trabajando (meses): {info['tiempo_trabajando']}")
    else:
        print("========== Empleados con menor tiempo en la empresa ==========")
        for id_empleado, info in empleados_menor_tiempo.items():
            print(f"Id: {id_empleado}")
            print(f"Nombre: {info['nombre']}")
            print(f"Tiempo trabajando (meses): {info['tiempo_trabajando']}")


def actualizar_salario_empleado(registro_empleados):
    try:
        print("========== Actualizar salario de un empleado ==========")
        id_empleado = input("Ingrese el Id del empleado: ")
        if id_empleado in registro_empleados:
            aumento = float(input("Ingrese el aumento que recibirá el empleado en soles: "))
            registro_empleados[id_empleado]['salario'] += aumento
            print(f"El nuevo salario del empleado con ID {id_empleado} es: S/ {registro_empleados[id_empleado]['salario']:.2f}")
        else:
            print("No se encontró un empleado con ese Id.")
    except ValueError:
        print("La entrada es inválida. Asegúrese de ingresar un número para el aumento.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def mostrar_menu():
    print("====================== Gestion de Empleados ========================")
    print("|| 1. Visualizar informacion de un empleado.                      ||")
    print("|| 2. Mostrar empleado cuyo tiempo en la empresa sea el menor     ||")
    print("|| 3. Actualizar salario de un empleado                           ||")
    print("|| 4. Terminar programa                                           ||")
    print("====================================================================")


def main():
    registro_empleados = {}
    registro_empleados = registrar_empleado(registro_empleados)

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elija la opcion que desee realizar (1/2/3/4): "))
            if opcion == 1:
                visualizar_informacion_empleado(registro_empleados)
            elif opcion == 2:
                mostrar_empleado_minimo_tiempo(registro_empleados)
            elif opcion == 3:
                actualizar_salario_empleado(registro_empleados)
            elif opcion == 4:
                print("Terminando el programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
