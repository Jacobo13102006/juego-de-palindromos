'''for i in range(1,10):
    print(i)'''
    
'''for i in range(10,0,-1):
    print(i)'''
    
'''for i in range(9,0,-1):
    print(i)'''
    
'''for i in 'jacobo'
    print(i)'''
    
'''for i in 'jacobo':
    print(i, end='')'''
    
'''for i in range(1,4):
    print(i,'jacobo')'''
    
'''estudiantes = ['alejo','manuela','jacobo','didier',11,'juanda','mateo','sebastian','jose luis']
for i in estudiantes:
    print(i, end=' ')'''
    


'''nombre = input('ingrese su nombre:  ')
edad = int(input('ingrese su edad:  '))'''

'''info =(edad,nombre)
for i in range(int(edad)):
    print(i+1,nombre,edad)'''
    
'''cree un programa que imprima los numeros pares del 1 al 100 y 
muestre un mensaje con su promedio'''

'''contador = 0 
print('los numeros pares son:')
for i in range(2,102,2):
    contador = contador + i
    promedio = contador /50
    print(i)

print(f'el promedio es {promedio}' )'''

'''escribir un programa que pida al usuario la 
contraseña, solo tiene 3 oportunidades, 
si la contraseña es incorrecta decir 
"contraseña incorrecta", cuando ingrese dar bienvenida, 
si ya cumplio el numero de intentos dar el mensaje perdiste tu oportunidad '''

contraseña = 'jacobo13'

for i in range(3):
    contraseña_usuario=input('ingrese la contraseña:  ')
    if contraseña == contraseña_usuario:
        print('contraseña correcta')
        print('bienvenido')
        break
    elif contraseña_usuario != contraseña:
        print('te haz equivocado')
else:
    print('perdiste la oportunidad')
        
        
    


        
    
    

    

    
