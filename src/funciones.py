drones=[]

def agregar_dron (id_dron, ubicacion, estado ):
    nuevo_dron={
        "ID":id_dron,
        "ubicacion": ubicacion,
        "estado": estado,
        "mision": None
    }
    drones.append(nuevo_dron)
    return drones

def eliminar_dron (id_dron):
    for dron in drones:
        if drones["ID"]== id_dron:
            drones.remove(dron)
            print(f"dron {id_dron} a sido eliminado")
            return
    print ("dron no encontrado")

def  asignar_mision(id_dron,nueva_ubicacion,nuevo_estado,mision):
    for dron in drones:
        if drones["ID"]==id_dron:
            drones["ubicacion"]=nueva_ubicacion
            drones["estado"]=nuevo_estado
            drones["mision"]=mision
            return
    print ("dron no encontrado, no se pudo agregar micion")

def actualizar_dron(id_dron, nueva_ubicacion,nuevo_estado):
    for dron in drones:
        if drones["ID"]==id_dron:
            drones["ubicacion"]=nueva_ubicacion
            drones["estado"]=nuevo_estado
            return
    print ("dron no encontrado, no se pudo actualizar la informacion")
        
def reporte_flota():
    for dron in drones:
        print(f"ID del dron{drones['ID']}\
                ubicacion{drones['ubicacion']}\
                estado{drones['estado']}\
                mision{drones['mision']}")
    return

