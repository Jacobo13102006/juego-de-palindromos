# >, <, >=, <=, ==, !=,
'''name1=input('Ingrese el primer nombre:  ')
name2=input('Ingrese el segundo nombre: ')'''



'''def nombres(name1:str, name2:str):
    
    if name1 != name2:
        print('Los nombres son diferentes')
    else:
        print('Los nombres son iguales')
        
nombres(name1, name2)'''

'''num1=int(input('ingrese el primer numero:    '))
num2=int(input('ingrese el segundo numero:   '))

def numeros(num1:int,num2:int):
    suma = num1 + num2
    print(f'La suma de los dos es:   {suma}')
   
    if num1 > num2:
        print(f'el {num1} es mayor que {num2}') 
    elif num1 == num2: 
        print('ambos numeros son iguales')
    else:
        print(f'el {num2} es mayor que {num1}')

numeros(num1,num2)'''


'''determinar si alguien es mayor de edad para ingresar a un bar, si tiene mas de 30 años se le da un bono'''
num1= int(input('Ingrese su edad por favor: '))
nombre = input('Ingrese su nombre:  ')

def edadpersonas(num1:int):
    if num1 < 18:
        print(f'Te llamas {nombre} y eres menor de edad tienes {num1} años no puedes ingresar ')
    elif  18<= num1 <= 29:
        print(f'Te llamas {nombre} y eres mayor de edad tienes {num1} años puedes ingresar ')
    else:
        print(f'Te llamas {nombre} y eres mayor de edad tienes {num1} años puedes ingresar y cuentas con un bono ')
        
edadpersonas(num1)
  
    
    





