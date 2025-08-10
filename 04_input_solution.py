
salario = input("Digite o valor do salário: ")
salario = float(salario)

aumento = float(input("Digite o percentual do aumento: "))

novo_salario = round(salario * (1 + (aumento / 100)), 2)
print(f"O salário de {salario} com {aumento}% de aumento é {novo_salario}")
