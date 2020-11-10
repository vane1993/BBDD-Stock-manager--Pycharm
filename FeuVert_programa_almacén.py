"""
Vanesa López García
23/05/2020
"""

from manager_db import Fabricante, Piezas, db
import csv

import pandas as pd

db.connect()


############################### FABRICANTE #####################################


########## Crear fabricante

def crear_fabricante():
    nombre_fabricante= input('Inserte el fabricante: ')
    n_registro_fabricante=  input('Inserte el numero de registro del fabricante: ')
    CIF_fabricante= input('Inserte el CIF: ')


    Fabricante.create(nombre_fabricante=nombre_fabricante, n_registro_fabricante=n_registro_fabricante,
                     CIF_fabricante=CIF_fabricante)
    print('El fabricante se ha creado correctamente')

#crear_fabricante()


######### Información fabricante
def info_fabricante():
    fabricante_nro = input('Inserte el numero de registro del fabricante que busca: ')
    for fabricante in Fabricante.select():
        if fabricante_nro == fabricante.n_registro_fabricante:
            print(f' Nombre del fabricante: {fabricante.nombre_fabricante}\n '
                  f'Número de registro: {fabricante.n_registro_fabricante}\n'
                  f'CIF: {fabricante.CIF_fabricante}')
#info_fabricante()


########### Modifiar Fabricante

def modificar_fabricante():

    nro_registro = input('Introduzca el numero de registro del fabricante que desee modificar: ')
    campo_modificar= input('Introduzca el campo que desee modificar y su nuevo valor <campo> <nuevo_valor>: ')

    split= campo_modificar.split(' ')
    campo= split[0]
    nuevo_valor= split[1]

    for fabricante in Fabricante.select():
        if fabricante.n_registro_fabricante == nro_registro:
            setattr(fabricante, campo, nuevo_valor)
            fabricante.save()
            break

    print('Actualizado ')



#modificar_fabricante()



############ Eliminar fabricante
def eliminar_fabricante():
    n_registro = input('Introduzca el numero de registro del fabricante que desee eliminar: ')
    eliminar_fabricante = Fabricante.delete().where(Fabricante.n_registro_fabricante == n_registro)
    eliminar_fabricante.execute()
    print('Se ha borrado correctamente')

#eliminar_fabricante()



###################################### PIEZAS  ######################

################### Crear pieza
def crear_pieza():

    nombre_piezas= input('Inserte el nombre de la pieza: ')
    n_registro_piezas = input('Inserte el numero de registro: ')
    fecha_fabricación= input('Inserte la fecha de fabricación (ej: 2020-05-10: ')
    fabricante= input('Inserte el nombre del fabricante: ')
    localidad_fabricacion =  input('Inserte la localidad de fabricación: ')
    precio = input('Inserte el precio: ')
    n_piezas_vendidas = input('Inserte el numero de piezas vendidas: ')

    Piezas.create(nombre_piezas=nombre_piezas, n_registro_piezas=n_registro_piezas, fecha_fabricación=fecha_fabricación,
                    fabricante= fabricante, localidad_fabricacion = localidad_fabricacion ,
                  precio= precio, n_piezas_vendidas=n_piezas_vendidas )

    print('La pieza se ha creado correctamente')

#crear_pieza()


################# Información pieza

def info_piezas():
    pieza_nro= input('Inserte el numero de registro de la pieza que busca: ')

    for pieza in Piezas.select():
        if pieza_nro == pieza.n_registro_piezas :
            print(f' {pieza.nombre_piezas}, {pieza.n_registro_piezas}, {pieza.fecha_fabricación},'
              f' {pieza.fabricante},{pieza.localidad_fabricacion}, {pieza.precio}, {pieza.n_piezas_vendidas}')

        else:
           print(f'La pieza no existe en el sistema')

#info_piezas()



######## Modificar Piezas

def modificar_pieza():

    nro_registro = input('Introduzca el numero de registro de la pieza que desee modificar: ')
    campo_modificar= input('Introduzca el campo que desee modificar y su nuevo valor <campo> <nuevo_valor>: ')

    split= campo_modificar.split(' ')
    campo= split[0]
    nuevo_valor= split[1]

    for pieza in Piezas.select():
        if pieza.n_registro_piezas == nro_registro:
            setattr(pieza, campo, nuevo_valor)
            pieza.save()
            break

    print('Actualizado correctamente')

#modificar_pieza()


############### Eliminar piezas

def eliminar_piezas():
    n_registro = input('Introduzca el numero de registro de la pieza que desee eliminar: ')
    eliminar_pieza= Piezas.delete().where(Piezas.n_registro_piezas == n_registro)
    eliminar_pieza.execute()
    print('Se ha borrado correctamente')
#eliminar_piezas()


######################### CARGAR DATOS ################


def get_data_piezas():
    lista_tuplas_piezas = []
    path= input('Inserte el path completo del archivo que desea cargar: ')
    with open(path, 'r') as piezas_file:
        contenido=csv.reader(piezas_file)
        next(contenido)
        for row in contenido:
            row = tuple(row)
            lista_tuplas_piezas.append(row)
    print(lista_tuplas_piezas)


def cargar_datos():

    print('Elija el tipo de datos que desee cargar:')
    print('-piezas')
    print('-fabricantes')

    while True:
        entrada= input('>>')
        if not entrada:
            print('')

        if entrada == 'exit':
            print('Gracias por su visita')


        elif entrada =='piezas':
            lista_tuplas_piezas = []

            with open('/Users/vanessalopezgarcia/Downloads/piezas.csv', 'r') as piezas_file:
                contenido = csv.reader(piezas_file)
                next(contenido)
                for row in contenido:
                    piezas_upper = list(map(lambda x: x.upper(), row))
                    # print(piezas_upper)

                    row = tuple(piezas_upper)
                    lista_tuplas_piezas.append(piezas_upper)
                    # print(lista_tuplas_piezas)

                Piezas.insert_many(lista_tuplas_piezas,
                                   fields=[Piezas.n_registro_piezas, Piezas.nombre_piezas, Piezas.fecha_fabricación,
                                           Piezas.fabricante, Piezas.localidad_fabricacion,
                                           Piezas.precio]).execute()
            print('Los datos se han cargado correctamente')
            break



        elif entrada == 'fabricantes':
            lista_tuplas_fabricante = []
            path=input('Inserte el path completo del archivo que desea cargar: ')
            #/Users/vanessalopezgarcia/Downloads/fabricantes.csv
            with open(path, 'r') as fabricante_file:
                contenido = csv.reader(fabricante_file)
                next(contenido)
                for row in contenido:
                    row_deleted = row.pop(2)
                    for item in row:
                        item= item.upper()
                        #print(row)

                    row = tuple(row)
                    lista_tuplas_fabricante.append(row)

                Fabricante.insert_many(lista_tuplas_fabricante, fields=[Fabricante.n_registro_fabricante,
                                                                        Fabricante.nombre_fabricante,
                                                                        Fabricante.CIF_fabricante]).execute()


            print('Los datos se han cargado correctamente')
            break

#cargar_datos()




################################################################
def cargar_piezas():
    lista_tuplas_piezas = []

    with open('/Users/vanessalopezgarcia/Downloads/piezas.csv', 'r') as piezas_file:
        contenido = csv.reader(piezas_file)
        next(contenido)
        for row in contenido:
            piezas_upper= list(map(lambda x: x.upper(), row))
            #print(piezas_upper)

            row = tuple(piezas_upper)
            lista_tuplas_piezas.append(piezas_upper)
            #print(lista_tuplas_piezas)

        Piezas.insert_many(lista_tuplas_piezas,fields=[Piezas.n_registro_piezas, Piezas.nombre_piezas, Piezas.fecha_fabricación,
                                                    Piezas.fabricante,Piezas.localidad_fabricacion,
                                                    Piezas.precio]).execute()
    print('Los datos se han cargado correctamente')

#cargar_piezas()


db.close()