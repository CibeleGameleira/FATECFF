#Solicitar do usuário uma determinada idade de um nadador.
#Baseado nesta idade indique qual a categoria ao qual ele pertence.

#Entrada de dados 
idade = int(input("Digite a idade: "))

#Testes

#Usando if simples com operador lógico

if (idade >=5 and idade <=7):
    print("Percente a categoria Infantil A") 
        
if (idade >=8 and idade <=10):
    print("Pertence a categoria Infantil B")
    
if (idade >=11 and idade <=13):
    print("Percente a categoria Juvenil A")
        
if (idade >=14 and idade <=17):
    print("Percence a categoria Juvenil B")       

if (idade >=18 and idade <=60):
    print("Percente a categoria Adulto")
    
if (idade <5):
    print("Não percence a nenhuma categoria")

if (idade >60):
    print ("Pertence a categoria Senior")
           
           
#Usando IF encadeado SEM operador lógico

if (idade <5):
    print("Sem categoria")

elif (idade <=7):
    print("Infantil A") 
        
elif (idade <=10):
    print("Infantil B")
    
elif (idade <=13):
    print("Juvenil A")
        
elif (idade <=17):
    print("Juvenil B")       

elif (idade <60):
    print("Adulto")
    
elif (idade >=60):
    print ("Senior")           