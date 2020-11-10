from manager_db import Fabricante, Piezas, db
from FeuVert_programa_almacén import crear_pieza, info_piezas, modificar_pieza,eliminar_piezas,crear_fabricante,info_fabricante, modificar_fabricante, eliminar_fabricante,  cargar_datos
from programa_ordenes_compra import crear_orden_compra, info_compra
from diccionario_queries import informe
#db.connect()





####################### MENU #########################




def mostrar_menu():
    """
    Muestra el menu principal
    """
    print('MENU PRINCIPAL\n'.center(0))

    print('Escriba "exit" si desea salir\n'.center(0))

    print('Buscar_pieza:'.center(0))
    print('-crear pieza'.center(20))
    print('-información pieza'.center(20))
    print('-modificar pieza'.center(20))
    print('-eliminar pieza\n'.center(20))

    print('Buscar fabricante'.center(0))
    print('-crear fabricante'.center(20))
    print('-información fabricante'.center(20))
    print('-modificar fabricante'.center(20))
    print('-eliminar fabricante\n'.center(20))

    print('Generar informe'.center(0))
    print('-Crear orden'.center(0))
    print('-Información orden\n'.center(0))



def main():
    """
    Funcion principal
    """
    print('\n\n\n')
    print('Bienvenido a nuestra base de datos'.center(0))
    print('\n\n\n')

    print('\n\n\n')
    print( 'Elija una opción: ')
    print('cargar datos'. center(20))
    print('ver menu'.center(20))

    while True:
        entrada= input('>>')
        if not entrada:
            print('')

        if entrada == 'exit':
            print('Gracias por su visita')
            break


        elif entrada== 'cargar datos':
            cargar_datos()
            break

        elif entrada== 'ver menu':
            mostrar_menu()



            while True:
                entrada= input('>>')
                if not entrada:
                    print('')


                #elif entrada == 'exit':
                    #print( 'Gracias por su visita')
                    #break

                elif 'crear pieza' in entrada:
                    crear_pieza()
                    break

                elif 'informacion pieza' in entrada:
                    info_piezas()
                    break

                elif 'modificar pieza' in entrada:
                    modificar_pieza()
                    print('Pieza modificada correctamente')
                    break

                elif 'eliminar pieza' in entrada:
                    eliminar_piezas()

                    break

                elif 'crear fabricante' in entrada:
                    crear_fabricante()

                    break

                elif 'informacion fabricante' in entrada:
                    info_fabricante()
                    break

                elif 'modificar fabricante' in entrada:
                    modificar_fabricante()
                    print('Fabricante modificado correctamente')
                    break

                elif 'eliminar fabricante' in entrada:
                    eliminar_fabricante()

                    break

                elif 'crear orden' in entrada:
                    crear_orden_compra()
                    print('Orden creada correctamente')
                    break

                elif 'informacion orden' in entrada:
                    info_compra()

                    break

                elif 'generar informe' in entrada:
                    informe()
                    print('informe generado con exito')
                    break



main()



db.close()