


def letras(palabra1:str, palabra2:str):
    iguales = []
    diferentes = []
    for i in palabra1:
        if i in palabra2:
            iguales.append(i)
        else:
            diferentes.append(i)
    encontradas = ''.join(iguales)
    print(f'las letras que se repiten en ambas palabras son {set(encontradas)}')
            
    for i in palabra2:
        if i not in palabra1:
            diferentes.append(i)
    no_encontradas = ''.join(diferentes)
    print(f'las letras diferentes son {set(no_encontradas)}')
           

        
palabra1 = input('ingrese la primera palabra: ')
palabra2 = input('ingrese la segunda palabra: ')


            
letras(palabra1,palabra2)


    

            
            
            