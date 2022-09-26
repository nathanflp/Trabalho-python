valorhora = float(input("\nDigite o valor da sua hora trabalhada: "))
horas = float(input("Digite quantas horas você trabalha: "))

salariobruto = (valorhora*horas)
inss = (salariobruto * 0.08)
irenda = (salariobruto * 0.11)
sindicato = (salariobruto * 0.05)
descontos = (inss+irenda+sindicato)
salarioliq = (salariobruto-descontos)

print(f"\n+ Salário bruto : R$",salariobruto)
print(f"- IR (11%) : R$",(round(irenda,2)))
print(f"- INSS (8%) : R$",(round(inss,2)))
print(f"- Sindicato (5%) : R$",(round(sindicato,2)))
print(f"= Salário Liquido : R$",(round(salarioliq,2)))

