
def menu ():

    print('\nMenu\n1.Agregar tarea\n2.Mostrar tareas\n3.Completar tarea\n4.Eliminar tarea\n5.Salir\n')
    opc = input('Selecciona una opcion:\n')

    if opc == '1':
        agregar_tarea()
    elif opc == '2':
        mostrar_tarea()
    elif opc == '3':
        pass
    elif opc == '4':
        pass
    elif opc == '5':
        pass
    else:
        print('Ingrese opciones validas (1-5).')

def agregar_tarea():

    tarea = input('Ingrese una tarea: ')
    lista_tareas.append(tarea)
    

def mostrar_tarea():

    print('Tareas Disponibles:\n')

    for i in range(len(lista_tareas)):
        print(f'{i+1}.{lista_tareas[i]}')


    

def completar_tarea():
    pass

def eliminar_tarea():
    pass


lista_tareas = []
activo = True

while activo:

    menu()
