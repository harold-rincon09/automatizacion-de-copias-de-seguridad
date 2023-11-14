import datetime 
import os 
import shutil

dt = datetime.datetime.now()

nombre = "copia de seguridad creada  {}_{}_{}_{}-{} ".format(dt.day,dt.month,dt.year,dt.hour,dt.minute)
shutil.make_archive(nombre,"zip","carpeta_de_copias_de_seguridad")

comienzo = []
total = os.listdir()

for a in total:
    if a.startswith("copia de seguridad creada el dia") == True:
        comienzo.append(a)

rutadestino = "D:/automatizacion de copias de seguridad"

for i in comienzo:
    shutil.move(i,rutadestino)

