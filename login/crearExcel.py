#openpyxl

from openpyxl import Workbook
from openpyxl.styles import Font

def crearExcel():
    
    #iniciar librerias para crear una hoja de calculo    
    book = Workbook()
    #Activar edición de la hoja de calculo
    sheet = book.active
    
    #seleccionar las columnas a las cuales le vamos a agregar info
    sheet['A1'] = "Id"
    sheet['B1'] = "Username"
    sheet['C1'] = "Password"
    sheet['D1'] = "Fecha de creación"
    
    #Damos diseño 
    sheet['A1'].font = Font(color = 'E91010', bold=True)
    sheet['B1'].font = Font(color = '2DE910', bold=True)
    sheet['C1'].font = Font(color = '10CFE9', bold=True)
    sheet['D1'].font = Font(color = 'E910C8', bold=True)
    
    #Guardamos el excel
    book.save('bd_login.xlsx')
    

crearExcel()
    
    
