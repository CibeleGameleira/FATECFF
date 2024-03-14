#Programa para calcular a média entre dois numeros


#Variaveis
num1 = num2 = soma = 0 #tipo inteiro
media = 0.0            #tipo real

#entrada de dados
# o int() já converte para inteiro
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

#calculando 
soma = num1 + num2
media = soma / 2.0 #2.0 força o resultado ser float

#exibir o resultado
print(f"A média é {media}")

      
