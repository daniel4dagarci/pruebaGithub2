import pruebavariables as var

def sumar (x,y):
    return x + y

def restar(x,y):
    return x - y

def multiplicar(x,y):
    return x * y

def dividir (x,y):
    if y == 0:
        return 'no se puede dividir entre 0'
    return x / y

def exit(): 
    return 'agur!!!!'

def calculadora():

    while True:

        print(var.msg2)

        opcion = int(input('opción: '))

        if opcion == 5: 
            exit()
            break

        n1 = int(input(var.val1))
        n2 = int(input(var.val2))

        if opcion == 1:
            resultado = sumar(n1,n2)
            print(f'el resultado de tu suma es {resultado}')
        
        elif opcion == 2:
            resultado = restar(n1, n2)
            print(f'el resultado de tu resta es {resultado}')
        
        elif opcion == 3:
            resultado = multiplicar(n1, n2)
            print(f'el resultado de tu multplicación es {resultado}')
        
        elif opcion == 4:
            resultado = dividir(n1, n2)
            print(f'el resultado de tu división es {resultado}')

        else: 
            print('opción no válida')
            continue