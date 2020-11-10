"""
Vanesa López García
23/05/2020
"""

from manager_db import Ordenes_compra, db
db.connect()

# crear orden de compra

def crear_orden_compra():

    ID_compra= input('Inserte el ID: ')
    fecha_compra= input('Inserte la fecha de compra (ej: 2020-05-10: ')
    vendedor= input('Inserte el vendedor: ')
    tupla_piezas =  input('Inserte las piezas que incluye la compra: ')
    precio_total = input('Inserte el precio total: ')

    Ordenes_compra.create(ID_compra=ID_compra, fecha_compra=fecha_compra,
                          vendedor=vendedor,
                    tupla_piezas= tupla_piezas, precio_total = precio_total )
#crear_orden_compra()


######## Informacion orden de compra

#for compra in Ordenes_compra.select():
#    print(f' {compra.fecha_compra}, {compra.vendedor},{compra.tupla_piezas, {compra.precio_total}')


def info_compra():
    identificador= input('Inserte el numero de identidad de compra: ')

    for compra in Ordenes_compra.select():
        if Ordenes_compra.ID_compra == identificador :
            print(f' {compra.ID_compra}, {compra.fecha_compra}, {compra.vendedor},{compra.precio_total}')

        else:
           print(f' El identificador no existe')

#info_compra()






db.close()