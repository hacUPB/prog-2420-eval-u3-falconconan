[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3

---

## Documentación del proyecto
Nombre:  Jacobo Restrepo Chavez
ID:  000418676

---
## seguimiento y control de flota de drones
este programa tiene como funcion hacer gestion y monitoreo de una flota de drones, lo que puede hacer mas facil el seguimiento de estos ademas de el conocimiento de como se encuentra la flota, el programa tendra funcionalidades como: 
- agregar drones a la flota
- asignar una mision al un dron activo y sin mision asignada
- actulizar la informacion de un dron posterior a la acignacion de una mision 
- eliminar un dron de la flota
- visualizar el estado de flota (drones activos, en mision,en mantenimiento)
En la industria aeroespacial, cada vez es más común utilizar drones para revisar infraestructuras clave zonas de difícil acceso. Contar con un sistema que gestion la flota mejora la eficiencia, optimisa recursos y asegura que las misiones se lleven a cabo de forma mas segura y organizada.
En el programa seutilizaran las siguientes estructuras de datos:
- Listas: Para almacenar la información de la flota de drones.
- Diccionarios: Para almacenar los detalles de cada dron.


```
inicio
    control=true
    mientras control=true
        imprimir(f"1. agregar un dron \n 2. eliminar un dron \n 3.asignar mision\n 4. actulizar dron sin asignar micion \n 5.reporte estado actual de la flota\n 6.salir")
        leer opcion
        si opcion == 1:
            id_dron = input("ID del dron: ")
            ubicacion = input("Ubicación del dron: ")
            estado = input("Estado del dron (disponible, en mantenimiento): ")
            agregar_dron(id_dron, ubicacion, estado) #funcion agregar dron 
            print(f"Dron {id_dron} agregado.")
            continuidad #funcion para determinar si desea haceralgo mas
        si-sino opcion == 2:
            id_dron = input("ID del dron: ")
            eliminar_dron(id_dron) #funcion de eliminar dron
            continuidad #funcion para determinar si desea haceralgo mas
        si-sino opcion == 3:
            id_dron = input("ID del dron: ")
            mision = input("Descripción de la misión: ")
            asignar_mision(id_dron, mision) #funcion para asignar mision
            continuidad #funcion para determinar si desea haceralgo mas
        si-sino opcion == 4:
            id_dron = input("ID del dron: ")
            nueva_ubicacion = input("Nueva ubicación (dejar en blanco para no cambiar): ")
            nuevo_estado = input("Nuevo estado (dejar en blanco para no cambiar): ")
            actualizar_dron(id_dron, nueva_ubicacion,nuevo_estado)
            continuidad #funcion para determinar si desea haceralgo mas
        si-sino opcion == 5:
            reporte_flotas #funcion de reporte de flota
            continuidad #funcion para determinar si desea haceralgo mas
        si-sino opcion == 6:
            imprimir (saliendo...)
            romper
        sino 
            imprimir (dato no valido vuelva a intentar)
fin
```