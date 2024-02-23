import random 





print('BIENVENIDOS AL JUEGO DE PALABRAS')

lista_palabras = ['casa','fango','maiz','computador','cable','celular','gay','papucho','shrek','nariz','pecas','venezuela']

seleccion = random.choice(lista_palabras)

x = list(seleccion)

random.shuffle(x)

print('Tu palabras es: ')
print(''.join(x))



for intento in range(2,-1,-1):
    intento_palabra = input('Ingresa la palabra que creas correcta:   ')
    if seleccion == intento_palabra:
        print(f'LO ADIVINASTE ES {seleccion} ')
        break
    elif seleccion != intento_palabra:
        print(f'intenta de nuevo fallaste, te quedan {intento} intentos')
    
        
    
else:
    print('La cagaste tonto, te quedaste sin intentos deja la paja')
    
