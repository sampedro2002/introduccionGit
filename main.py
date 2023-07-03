print("hello wordl")
a = int(input("Ingrese un numero entero i: "))
b = int(input("Ingrese un numero entero ii: "))
suma = a + b
print("La suma resultante es: ",{suma})
print("El resultado de la resta es: ",{a-b})

print("En este casi comensaremos a probar el historial")

#Prueba 1
#Una combinacion entre condicional y bucle
try:
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero : "))
    res = num1/num2
    print("El resultado de la division de ", num1, " y ", num2, " es: ",res)

except ValueError:
    print("Error: Debes ingresar numeros esteros")
except ZeroDivisionError:
    print("Erro: No se puede dividir entre cero.")

print("Fin de la prueba")

print("Esta sera la prueba 2")
