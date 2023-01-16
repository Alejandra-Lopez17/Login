from openpyxl import *
from openpyxl import Workbook
from datetime import date


def crearUsuario():
    #Iniciamos el excel 
    book = load_workbook('bd_login.xlsx')
    
    #recuperamos la cantidad de filas de nuestro código
    max_row = book.active.max_row
    
    print(max_row)
    
    #Datos de los usuarios para guardar en la bd para que luego se puedan logear
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese contraseña(mayor de 5 digitos)(con letras y numeros): ")
    confirPassword = input("confirme su contraseña: ") 
    
    #confirmamr las contraseñas
    if password == confirPassword and len(password) > 5:
        #agregar id
        sheet = book.active
        sheet[f"A{max_row+1}"] = max_row
        
        #agregar username
        sheet = book.active
        sheet[f"B{max_row+1}"] = username
        
        #agregar password
        sheet = book.active
        sheet[f"C{max_row+1}"] = password
        
        
        #agregar fecha de creación
        sheet = book.active
        sheet[f"D{max_row+1}"] = date.today()
        
        #guardar el excel
        print("Usuario registrado")
        book.save('bd_login.xlsx')      
        
    
    else:
        print("contraseña no valida")  
    
crearUsuario()
    
