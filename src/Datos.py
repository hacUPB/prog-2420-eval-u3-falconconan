from funciones import *

def main():
    drones=[]
    while True:
        print("\n--- Gestión de Flotas de Drones ---")
        print("1. Agregar dron")
        print("2. Asignar misión")
        print("3. Actualizar dron")
        print("4. Eliminar dron")
        print("5. Generar reporte")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id_dron = input("ID del dron: ")
            ubicacion = input("Ubicación del dron: ")
            estado = input("Estado del dron (disponible, en mantenimiento): ")
            agregar_dron(id_dron, ubicacion, estado)
            print(f"Dron {id_dron} agregado.")

        elif opcion == '2':
            id_dron = input("ID del dron: ")
            mision = input("Descripción de la misión: ")
            nueva_ubicacion = input("ubicacion de la mision: ")
            nuevo_estado = input("Descripcion del nuevo estado: ")
            asignar_mision(id_dron,nueva_ubicacion,nuevo_estado,mision)

        elif opcion == '3':
            id_dron = input("ID del dron: ")
            nueva_ubicacion = input("Nueva ubicación (dejar en blanco para no cambiar): ")
            nuevo_estado = input("Nuevo estado (dejar en blanco para no cambiar): ")
            actualizar_dron(id_dron, nueva_ubicacion , nuevo_estado)

        elif opcion == '4':
            id_dron = input("ID del dron a eliminar: ")
            eliminar_dron(id_dron)

        elif opcion == '5':
            reporte_flota()

        elif opcion == '6':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")



if __name__ == "__main__":
    main()
