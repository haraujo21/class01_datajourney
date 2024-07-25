# 1 - Solicite o nome do usuário
nome = input("Nome: ")

# 2 - Receba salário:
salario = float(input("Digite salario:"))

# 3 - Receba bonus:
bonus = float(input("Digite bonus:"))

valor_bonus = 1000 + salario*bonus

# 4
print(f"R$ {valor_bonus}")

# 5
print(f"Seu valor total será de: {valor_bonus}")
