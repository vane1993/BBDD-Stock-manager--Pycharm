"""
Vanesa López García
23/05/2020
"""

from peewee import *
from playhouse.migrate import SqliteMigrator, migrate
db= SqliteDatabase('FeuVert_db')


class Fabricante(Model):

    nombre_fabricante = CharField(null=True)
    n_registro_fabricante= CharField(null=True)
    CIF_fabricante = CharField()

    class Meta:
        database=db


class Piezas(Model):

    nombre_piezas= CharField()
    n_registro_piezas= CharField(null=True)
    fecha_fabricación = DateTimeField(null=True)

    localidad_fabricacion = CharField(null=True)
    precio= FloatField()
    n_piezas_vendidas= IntegerField(null=True)
    fabricante = ForeignKeyField(Fabricante,
                                 db_column='fabricante',
                                 field=Fabricante.nombre_fabricante,

                                 null=True,
                                 on_delete='SET NULL',
                                 backref='piezas')

    # Columna que relaciona piezas con el fabricante
    #dato_fabricante= ForeignKeyField(Fabricante,
                                    # db_column='dato_fabricante',
                                     #null=True,
                                     #on_delete= 'SET NULL',
                                     #backref='piezas')
    class Meta:
        database= db


class Ordenes_compra(Model):

    ID_compra= CharField()
    fecha_compra= DateTimeField()
    vendedor= CharField()
    tupla_piezas= ()
    precio_total = FloatField()

    class Meta:
        database= db



def create_conection():
    db.connect()
    db.create_tables([Fabricante,Piezas,Ordenes_compra])
    db.close()

create_conection()







######## MIGRACION PARA ESTABLECER RELACION ENTRE FABRICANTE Y PIEZAS ###########

#def run_migration_fabricante():
    #db.connect()
    #migrator= SqliteMigrator(db)

    #with db.transaction():
       # migrate(
           # migrator.add_column('piezas',
                               # 'dato_fabricante',
                               # ForeignKeyField(Fabricante,
                                               # field= Fabricante.id,
                                               # null=True,
                                               # on_delete= 'SET NULL',
                                               # backref='piezas'))
     #   )
    #print('Migración concluída')
    #db.close()
#run_migration_fabricante()







