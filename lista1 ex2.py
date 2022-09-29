pesopeixes = float(input("\nDigite a quantidade de kilos de peixes pescados: "))
excesso = pesopeixes - 50

print(f"\nVocê pescou ",pesopeixes,"kilos de peixe")

if(excesso>=0):

    multa = excesso * 4
    print(f"A quantidade de peixe excedente foi de:",excesso,"Kilos")
    print(f"O valor da multa será de: R$",multa)

else:

    multa = 0
    print(f"A quantidade limite de peixe não foi excedida, multa não aplicada :)")
