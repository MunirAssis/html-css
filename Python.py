valor = int(input("qual valor desejado: "))

cem = valor // 100
resto = valor % 100

cinquenta = resto // 50
resto1 = resto % 50

vinte = resto1 // 20
resto2 = resto1 % 20

dez = resto2 // 10

print("o valor é de", cem, "notas de 100 reais")
print("o valor é de", cinquenta, "notas de 50 reais")
print("o valor é de", vinte, "notas de 20 reais")
print("o valor é de", dez, "notas de 10 reais")
print("O problema foi resolvido")

concatenacao = "py" + "thon"
repeticao = "py" * 3