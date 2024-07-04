import os
os. system('cls')

lista = []

def grabarp():
    nif=input('ingrese numero de identificacion fiscal(formato de: 8 digitos, guion y 3 letras \nEjemplo: 01234567-ESP): ')
    nombre=input('ingrese nombre: ')
    edad=int(input('ingrese edad: '))
    persona = {
        "nif": nif,
        "nombre":nombre,
        "edad":edad
    }
    lista. append(persona)
    
def buscarp():
    nif=input('ingrese el NIF a buscar: ')
    for persona in lista:
        if persona ['nif'] == nif:
            print("datos de persona: ")
            print(f"{persona}")
    
def imprimircert():
    print('Imprimir Certificado')
    
def salir():
    print('Lo vimoh...')
    
    
        
while True:
    print('--Menu--')
    print('1.Grabar')
    print('2.Buscar')
    print('3.Imprimir certificados')
    print('4.Salir')
    op=int(input('ingrese opcion: '))
    
    if op == 1:
        grabarp()
        
    elif op == 2:
        buscarp()
        
    elif op ==3:
        imprimircert()
        
    elif op ==4:
        salir()
        break
    
    else:
        print('Opcion invalida')