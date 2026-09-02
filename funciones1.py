#sumar dos numeros y mostrar el resultado
def getsum(number1, number2):
    return number1 + number2

def showResult(message, result):
    return f"{message} {result}" 

print("Dime un numero: ")
num1 = float(input())
print("Dime otro numero: ")
num2 = float(input())
sum = getsum(num1, num2)
print(showResult("La suma es:", sum))
