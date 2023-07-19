var_verdade = True # Boolean
var_falso = False

if var_verdade:
    print("Var_verdade é verdadeiro\n")

a = 2
b = 1

if a > b:
    print(a, "é maior do que", b)
else:
    print(a, "não é maior do que", b)

print()  # quebra de linha

print("opcoes:\n1 = escreve guilherme\n2 = escreve joao\n3 = escreve maria")
opcao = input("Escolha uma opcao: ")

if opcao == "1":
    print("guilherme")
elif opcao == "2":
    print("joao")
elif opcao == "3":
    print("maria")
else:
    print("Opcao invalida\n")

"""
Faça um programa que pergunte a idade, peso e altura de uma pessoa e decide se ela está apta a ser do exercito.
Para entrar no exercito, a pessoa tem que ter mais de 18 anos, mais ou igual 60kg e medir mais ou igual 1.70m!
"""
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

if idade > 18 and peso >= 60 and altura >= 1.70:
    print("Apto!")
else:
    print("Inapto!")
