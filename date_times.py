'''import datetime

fecha = datetime.datetime.now()

fecha_futura = fecha + datetime.timedelta(days=9)

nuevo_formato = fecha_futura.strftime('%d - %B - %Y')

print(nuevo_formato)'''

"realizar una funcion que me imprima cual fue la fecha hace 1000 dias"


'''import datetime

fecha = datetime.datetime.now()

fecha_pasada = fecha + datetime.timedelta(days= -100)

nuevo_formato = fecha_pasada.strftime(' %d - %B - %Y')

print(nuevo_formato)'''


''' funcion que al ingresar una fecha diga la edad de la personas'''

import datetime

def calculo_edad(año:int, mes:int, dia:int):
    
    fecha_persona = datetime.datetime(año, mes, dia)
    fecha_actual = datetime.datetime.now()
    edad = fecha_actual- fecha_persona
    edad_en_años = edad // 365
    
    

    print(f' su edad es {edad_en_años.days} años')

año = int(input(' ingrese su año de nacimiento '))
mes = int(input(' ingrese su mes de nacimiento '))
dia = int(input(' ingrese su dia de nacimiento '))
 
calculo_edad(año, mes,dia)
    

    
    

