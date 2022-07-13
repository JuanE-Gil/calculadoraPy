# IMPORTAMOS LOS PAQUETES NECESARIOS
import os
import sys
import math

#  CREAMOS EL MENÚ DE OPCIONES
def menu():

  while True:

    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ~~ MENÚ DE OPCIONES ~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print('[1] SUMAR')
    print('[2] RESTAR')
    print('[3] MULTIPLICAR')
    print('[4] DIVIDIR')
    print('[5] Raiz Cuadrada')
    print('[6] AlCuadrado')
    print('[7] POTENCIA')
    print('[EXIT] SALIR')

    print('')
    opc = input('Elija una opción: ')
    print('')

    if opc == '1':
      # print('SUMANDO\n')
      Sumar()
    if opc == '2':
      # print('RESTANDO\n')
      Restar()
    if opc == '3':
      # print('MULTIPLICANDO\n')
      Multiplicar()
    if opc == '4':
      # print('DIVIDIENDO\n')
      Dividir()
    if opc == '5':
        RaizCuadrada()
      # print('RAIZCUADRADA\n')
    if opc == '6':
      AlCuadrado()
      # print('ALCUADRADO\n')
    if opc == '7':
      Potencia()
      # print('POTENCIA\n')
    if opc == 'exit':
      # print('SALIENDO\n')
      sys.exit()
      
    print('')
    input('ENTER para continuar')
  

#  CREAMOS LAS FUNCIONES
def Sumar():
  os.system("cls")
  print('~~~~~~~~~~~~~~~~~')
  print('| ~~ SUMANDO ~~ |')
  print('~~~~~~~~~~~~~~~~~')
  Num1 = float(input('Ingrese el primer número para sumar: '))
  Num2 = float(input('Ingrese un segundo número para sumar: '))
  Result = Num1 + Num2
  print('El resultado de la Suma es:',Result)


def Restar():
  os.system("cls")
  print('~~~~~~~~~~~~~~~~~~')
  print('| ~~ RESTANDO ~~ |')
  print('~~~~~~~~~~~~~~~~~~')
  Num1 = float(input('Ingrese el primer número para la resta: '))
  Num2 = float(input('Ingrese un segundo número para la resta: '))
  Result = Num1 - Num2
  print('El resultado de la Resta es:',Result)

def Multiplicar():
  os.system("cls")
  print('~~~~~~~~~~~~~~~~~~~~~~~')
  print('| ~~ MULTIPLICANDO ~~ |')
  print('~~~~~~~~~~~~~~~~~~~~~~~')
  Num1 = float(input('Ingrese el primer número para la multiplicación : '))
  Num2 = float(input('Ingrese un segundo número para la multiplicación: '))
  Result = Num1 * Num2
  print('El resultado de la Multiplicación es:',Result)

def Dividir():
  os.system("cls")
  print('~~~~~~~~~~~~~~~~~~~~')
  print('| ~~ DIVIDIENDO ~~ |')
  print('~~~~~~~~~~~~~~~~~~~~')
  Num1 = float(input('Ingrese el primer número para dividir : '))
  Num2 = float(input('Ingrese un segundo número para la division: '))
  Result = Num1 / Num2
  print(f'El resultado de la Division es: {Result :.2f}')

def RaizCuadrada():
  os.system("cls")
  print('~~~~~~~~~~~~~~~~~~~~~~~~~')
  print('| ~~ RAIZ CUADRADADA ~~ |')
  print('~~~~~~~~~~~~~~~~~~~~~~~~~')
  Num1 = float(input('Ingrese el número al que quisiera ver su Raiz Cuadrada : '))
  print(f"{math.sqrt(Num1):2f}")

def AlCuadrado():
  os.system("cls")
  print('~~~~~~~~~~~~~~~~~~~~~')
  print('| ~~ AL CUADRADO ~~ |')
  print('~~~~~~~~~~~~~~~~~~~~~')
  Num1 = float(input('Ingrese el número para ver su cuadrado: '))
  Result = Num1 ** 2
  print(f'{Num1} al cuadrado es: {Result}')

def Potencia():
  os.system("cls")
  Num1 = float(input('Ingrese el número para elevarlo: '))
  x = float(input('Ingrese el número al que quiere elevar: '))
  Result = math.pow(Num1, x)
  print(f'{Num1} a la potencia {x} es igual a: {Result}')


menu()