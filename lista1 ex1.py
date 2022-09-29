altura = float(input("\nInforme sua altura = "))
print("\n1 - Homem | 2 - Mulher")
sexo = int(input("informe seu sexo = "))

while sexo !=1 and sexo !=2: #loop caso sexo seja diferente do solicitado

        print("\nDados inválidos,tente novamente!\n" "\n1 - Homem | 2 - Mulher")
        sexo = int(input("informe seu sexo = "))

if(sexo == 1): #Caso 1 Homem

        pesoIdeal = 72.7 * altura - 58
        print(f"\nSeu peso ideal é de: {(round(pesoIdeal,1))} Kg(s)")

elif(sexo == 2): #Caso 2 Mulher
        
        pesoIdeal = 62.1 * altura - 44.7
        print(f"\nSeu peso ideal é de: {(round(pesoIdeal,1))} Kg(s)")
        
