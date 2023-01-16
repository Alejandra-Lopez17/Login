from openpyxl import *
from openpyxl import Workbook

def loginUsuario():
    #iniciar el excel
    book = load_workbook('bd_login.xlsx')
    
    #recuperar la cantidad de filas
    max_row = book.active.max_row
    
    #datos del usuario para comprobar que ya estén registrados en la bd
    
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    
    #rastrear los usuarios de la base de datos
    sheet = book.active
    for i in range(max_row):
        #iniciamos en la fila 2
        variableApoyo = i+2
        
        userconfi = sheet[f"B{variableApoyo}"]
        passConfi = sheet[f"C{variableApoyo}"]
        
        if username == userconfi.value:
            if password == passConfi.value:
                print("el usuario está logeado")
                return True
         
    else:
        print("contraseña o usuario incorrectos")
               

loginUsuario()        

