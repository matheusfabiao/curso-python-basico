# Built-in functions
print("Hello World!")

print(len("Hello World!"))

# input('Digite algo: ')


# Criar funções
# Com retorno e com argumentos
def soma(numero1, numero2):
    res = numero1 + numero2
    return res


retorno = soma(2.5, 2.5)
print(retorno)


# Sem retorno e sem argumentos
def imprime_oi():
    print('Oi')


imprime_oi()


def tem_sete_itens(objeto):
    if len(objeto) == 7:
        return True
    else:
        return False


if tem_sete_itens('1234567'):
    print('Realmente tem 7 letras')

if tem_sete_itens([1, 2, 3, 4, 5, 6, 7]):
    print('Realmente tem 7 letras')

# OBS: FUNÇÃO != MÉTODO
# Função = há um tipo de retorno
# Método = não há retorno

"""
EXERCICIO: Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior número dentro dessa coleção
"""


def add_lista():
    i = 0
    while i < repeticoes:
        numero = int(input('Digite um número: '))
        numeros.append(numero)
        i += 1


def maior_num(lista):
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior


numeros = []
repeticoes = int(input('Digite o número de repetições: '))

add_lista()
print(maior_num(numeros))
