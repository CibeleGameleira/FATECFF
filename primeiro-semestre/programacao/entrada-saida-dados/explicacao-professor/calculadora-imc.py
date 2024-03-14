#Calculo do IMC 


# define as variaveis 

imc = peso = altura = 0.0 #define como float 

#Entrada de dados 

peso = float(input("Informe o peso: ")) 
altura = float(input("Informe a altura: "))

#calcular o IMC

imc = peso / altura ** 2

#fazendo a verificação 
if (imc > 30) :
    print("Resultado: Acima do peso")
else :
    # O \n faz pular uma linha 
    print(f"Seu IMC é {imc:3.3f} \nResultado: Normal")
    print"(Seu IMC é {imc} \nResultado: Normal")
    print("Seu IMC é %f calculado" % imc)
    print("Seu IMC é", imc, "calculado")      
    print ("Seu IMC é %3.3f calulado" % imc")
    print ('Seu IMC é {3.3f} calculado