# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:51 2022

@author: Frank
"""

archivo=open("archivo_de_prueba.txt","wt")
contenido="Línea1 hola amigos ¿Cómo están?\nLínea2 Bienvenidos a la Untels."
archivo.write(contenido)
archivo.close()