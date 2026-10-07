"""'''Exercico 1'''
anterior = float(input("Consumo do mês anterior (m³): "))
atual = float(input("Consumo do mês atual (m³): "))
 
if atual <= 20:
    preco = 2.00
elif atual <= 35:
    preco = 3.50
elif atual <= 50:
    preco = 5.50
else:
    preco = 7.00

valor_consumo = atual * preco
print(f"Valor do consumo: R$ {valor_consumo:.2f}")

if atual < anterior:
    desconto = valor_consumo * 0.15
    total = valor_consumo - desconto
    print(f"Desconto: R$ {desconto:.2f}")
elif atual > anterior:
    multa = valor_consumo * 0.10
    total = valor_consumo + multa
    print(f"Multa: R$ {multa:.2f}")
else:
    total = valor_consumo

print(f"Total da conta: R$ {total:.2f}")

'''Exercicio 2'''

login = input("informe o login: ")
senha = input("informe a senha: ")

if login == "scott":
    if senha == "tiger":
        print("autenticado com sucesso")
    else:
        print("usuario ou senha inválida")

elif login == "walt":
    if senha == "disney":
        print("autenticado com sucesso")
    else:
        print("usuario ou senha inválida")

elif login == "spock":
    if senha == "ncc1701":
        print("autenticado com sucesso")
    else:
        print("usuario ou senha inválida")

else:
    print("usuario ou senha invalido")
    
    
'''Exercicio 3'''

peso = int(input("informe seu peso (Kg): "))
altura = float(input("informe sua altura (m): "))

Imc = peso / (altura * altura)

if Imc < 18.5:
    print("Abaixo do peso")
elif Imc <= 24.9:
    print("peso normal")
elif Imc <=29.9:
    print("sobrepeso")
else:
    print("Obesidade")"""


'''Exercicio 4'''

"""num = int(input("insira um numero: "))

while num > 1:

    dig = num % 10
    if dig % 2 == 0:
        print(f"{dig} é par")
    else:
        print(f"{dig} é impar")

    num = num // 10"""

'''Exercicio 5 - Urna'''

voto = int(input(" informe seu voto: \n 0 - encerrar votação \n 1 - candidato A \n 2 -  candidato B \n 3 - Voto nulo \n4 Voto em Branco:" ))

cadA = 0
cadB = 0
nulo = 0
branco = 0

while voto != 0:
    if voto == 1:
        cadA = cadA + 1
    elif voto ==2:
        cadB = cadB + 1
    elif voto == 3:
        nulo = nulo + 1
    elif voto == 4:
        branco = branco + 1
    else:
        Print("Opção invalida")

print(f"====Apuração dos votos====\n Candidato A com: {cadA} votos \n Candidato B com: {cadB} votos\n nulos : {nulo} \n brancos: {branco}" )