#Entrada de dados
numero = int(input("Digite um número qualquer:"))

#Testes

if   (numero >=0 and numero <=10):
    print("O número está na Faixa 1")
elif (numero >= 15 and numero <=25):
    print ("O número está na Faixa 2")   
elif (numero >= 26 and numero <=40):    
    print ("O número está na Faixa 3")
else:
    print("O número não está em nenhuma Faixa")  
    
#outra forma  

if (numero >= 15 and numero <10):
    print("O número está na Faixa 1")
else:
   if (numero >= 15 and numero <=25):
    print("O número está na Faixa 2")
   else:
     if (numero >=26 and numero <=40):
        print("O número não está em nenhuma faixa")
        
       
    