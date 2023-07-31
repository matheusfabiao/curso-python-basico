nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']
for nome in nomes:
    print(nome)

for item in range(0, 100, 2):
    print(item)

for i in range(len(nomes)):
    print(nomes[i])

palavra = 'Matheus Fabião'
for letra in palavra:
    print(letra)

i = 0
while i < 10:
    print('i ainda é menor do que 10!')
    i += 1
print('Acabou o while: ', i)

numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1

'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa. Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados. Após isso irá imprimir todos os nomes da lista.
'''
convidados = list()
nome = ''
while True:
    nome = input('Digite o nome do convidado: ').capitalize()
    convidados.append(nome)
    opcao = input('Deseja continuar? [S/N]').upper()
    if opcao == 'N':
        break
    i += 1
print(f'Lista de convidados: {convidados}')
