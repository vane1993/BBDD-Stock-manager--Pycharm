import peewee
from peewee import *
from peewee import fn

from manager_db import Fabricante, Piezas, db, Ordenes_compra
import datetime
db.connect()

#1   Número de piezas vendidas

total= []
for pieza in Piezas.select():

    print(pieza.n_piezas_vendidas)
    pieza_vendida= pieza.n_piezas_vendidas

    total.append( pieza_vendida)

    piezas_vendidas= sum(total)

print(f'Número de piezas vendidas: {piezas_vendidas}')


#2 Ingresos totales por la venta de piezas
total=[]

for pieza in Piezas.select():
    pieza_vendida= pieza.n_piezas_vendidas
    precio_pieza= pieza.precio
    precio_total= pieza_vendida * precio_pieza
    total.append( precio_total)
    ingresos_totales= sum(total)

print(f'Ingresos totales: {ingresos_totales}')

#3 Fabricante más vendido
lista_numero_piezas=[]
for pieza in Piezas.select():
    lista_numero_piezas.append(pieza.n_piezas_vendidas)
maximo_vendido= max(lista_numero_piezas)


fabricante_piezas = Fabricante.select().join(Piezas).where(Piezas.n_piezas_vendidas == maximo_vendido)

for fabricante in fabricante_piezas:
    print(f'{fabricante.nombre_fabricante}')


#4 Fabricante menos vendido

lista_numero_piezas=[]
for pieza in Piezas.select():
    lista_numero_piezas.append(pieza.n_piezas_vendidas)
minimo_vendido= min(lista_numero_piezas)


fabricante_piezas = Fabricante.select().join(Piezas).where(Piezas.n_piezas_vendidas == minimo_vendido)

for fabricante in fabricante_piezas:
    print(f'{fabricante.nombre_fabricante}')




#5 Fabricante cuyas piezas son más caras

lista_precio_piezas=[]
for pieza in Piezas.select():
    lista_precio_piezas.append(pieza.precio)
pieza_mas_cara= max(lista_precio_piezas)

fabricante_piezas = Fabricante.select().join(Piezas).where(Piezas.precio == pieza_mas_cara)

for fabricante in fabricante_piezas:
    fabricante_mas_caro= fabricante.nombre_fabricante
print(f'El fabricante más caro es: {fabricante_mas_caro}')
print(f'{fabricante.nombre_fabricante}')


#6  En qué época del año de fabrican mas piezas (invierno, primavera,verano, otoño)
winter = datetime.datetime.strptime("2020-01-01",  "%Y-%m-%d")
spring = datetime.datetime.strptime("2020-3-21",   "%Y-%m-%d")
summer = datetime.datetime.strptime("2020-6-21", "%Y-%m-%d")
fall = datetime.datetime.strptime("2020-9-21","%Y-%m-%d")
winter_2 = datetime.datetime.strptime("2020-12-21",  "%Y-%m-%d")


#for pieza in Piezas.select().group_by(Piezas.fecha_fabricación):
    #fecha = str(pieza.fecha_fabricación)
    #fecha_by_string = datetime.datetime.strptime(fecha, '%d/%m/%Y %H:%M:%S')
    #pieza.fecha_fabricación = datetime.datetime.strptime(fecha, '%d/%m/%Y %H:%M:%S')

    #if pieza.fecha_fabricación > winter and pieza.fecha_fabricación < spring:
        #pieza.fecha_fabricación = 'winter'

    #elif pieza.fecha_fabricación > spring and pieza.fecha_fabricación <summer:
        #pieza.fecha_fabricación= 'spring'

    #elif pieza.fecha_fabricación > summer and pieza.fecha_fabricación <fall:
        #pieza.fecha_fabricación= 'summer'

    #elif pieza.fecha_fabricación > fall and pieza.fecha_fabricación < winter_2:
        #pieza.fecha_fabricación= 'summer'
    #print(f'{pieza.fecha_fabricación} - {pieza.n_registro_piezas}')


    #lista_winter=[]
    #if pieza.fecha_fabricación == 'winter' in  pieza.fecha_fabricación:
        #lista_winter.append(pieza.fecha_fabricación)
        #print(lista_winter)



#7 En qué época del año de venden mas piezas (invierno, primavera,verano, otoño)

winter = datetime.datetime.strptime("2020-01-01",  "%Y-%m-%d")
spring = datetime.datetime.strptime("2020-3-21",   "%Y-%m-%d")
summer = datetime.datetime.strptime("2020-6-21", "%Y-%m-%d")
fall = datetime.datetime.strptime("2020-9-21","%Y-%m-%d")
winter_2 = datetime.datetime.strptime("2020-12-21",  "%Y-%m-%d")


#for pieza in Piezas.select().group_by(Piezas.fecha_fabricación):
    #fecha = str(pieza.fecha_fabricación)
    #fecha_by_string = datetime.datetime.strptime(fecha, '%d/%m/%Y %H:%M:%S')
    #pieza.fecha_fabricación = datetime.datetime.strptime(fecha, '%d/%m/%Y %H:%M:%S')

    #if pieza.fecha_fabricación > winter and pieza.fecha_fabricación < spring:
        #pieza.fecha_fabricación = 'winter'

    #elif pieza.fecha_fabricación > spring and pieza.fecha_fabricación <summer:
        #pieza.fecha_fabricación= 'spring'

    #elif pieza.fecha_fabricación > summer and pieza.fecha_fabricación <fall:
        #pieza.fecha_fabricación= 'summer'

    #elif pieza.fecha_fabricación > fall and pieza.fecha_fabricación < winter_2:
        #pieza.fecha_fabricación= 'summer'
    #print(f'{pieza.fecha_fabricación} - {pieza.n_registro_piezas}')






#8  Listado completo de locaciones de fabricación de piezas, ordenado alfabéticamente.

listado_localizaciones=[]
for piezas in Piezas.select():
    listado_localizaciones.append(piezas.localidad_fabricacion)
localizaciones = sorted(listado_localizaciones)
print(localizaciones)



#9. Listado completo de fabricantes ordenados por su número de registro.
listado_fabricantes=[]
for fabricante in Fabricante.select().order_by(Fabricante.n_registro_fabricante):

    listado_fabricantes.append(fabricante.nombre_fabricante)
fabricantes = listado_fabricantes
print(fabricantes)


#10 El empleado del mes (vendedor con más compras)

#data= (Ordenes_compra.select(Ordenes_compra.vendedor, fn.COUNT(Ordenes_compra.ID_compra).alias('COMPRAS')).group_by(Ordenes_compra.vendedor)
#for vendedor in data:
    #print(f'{vendedor.vendedor}- {vendedor.ID_compra}')


