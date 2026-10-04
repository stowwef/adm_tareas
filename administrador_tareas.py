
def menu ():

    print('\n----- Menu -----\n1.Agregar tareas\n2.Mostrar tareas\n3.Completar tarea\n4.Eliminar tarea\n5.Salir\n')
    opc = input('Selecciona una opcion:\n')

    if opc == '1':
        agregar_tarea()
    elif opc == '2':
        mostrar_tarea()
    elif opc == '3':
        pass
    elif opc == '4':
        eliminar_tarea()
    elif opc == '5':
        pass
    else:
        print('Ingrese opciones valida (1-5).')

def agregar_tarea():

    print('\n----- Agregar Tarea -----')
    cant_tareas = int(input('\nCuantas tareas desea agregar?\n'))

    for tarea in range(cant_tareas):

        tareas = input(f'#{tarea+1} tarea: ')
        lista_tareas.append(tareas)
    else:
        print('\nLas Tareas fueron agregadas sastifactoriamente ;D')

def mostrar_tarea():

    contador_items = 0

    print('--- Mostrar Tareas ----\n')

    print('Tareas Disponibles:\n')

    for i in range(len(lista_tareas)):
        print(f'{i+1}. {lista_tareas[i]}')
        contador_items += 1

    print(f'\nActualmente hay {contador_items} items.')

def completar_tarea():
    pass

def eliminar_tarea():
    print('\n----- Eliminar Tareas ----')
    opc_eliminar = int(input('\n1.Eliminar todas las tareas\n2.Eliminar una tarea\n3.Eliminar rango de tareas\n'))

    if opc_eliminar == 1:

        lista_tareas.clear()

    elif opc_eliminar == 2:

       print('\nTareas Disponibles: ')
        
       for x in range(len(lista_tareas)):
            
            print(f'{x+1}. {lista_tareas[x]}')
            

       i = int(input('\nCual tarea deseas eliminar? Ingrese #\n'))
       i = i - 1
       del lista_tareas[i]

    elif opc_eliminar == 3:
        pass
        '''
        print('\nTareas Disponibles: ')
        
        for x in range(len(lista_tareas)):
            
         print(f'{x+1}. {lista_tareas[x]}')

        print('\nSeleccione el rango de tareas:')
        punto_inicio = int(input('Desde: '))
        punto_final = int(input('Hasta: '))

        rango = []
        punto_final = p

        for r in range(punto_final,1):
            rango.append(r) 

        for item in rango:

            del lista_tareas[item]

        else:
            print('\nItems eliminados exitosamente :D')
    else:
        print('Ingrese un valor valido (1-2)')
        '''

def salir_menu():
    pass

lista_tareas = []
activo = True

while activo:

    menu()
