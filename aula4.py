frase = 'Oi, tudo bem?'
lista_nomes = ['Joao', 'Maria', 'Guilherme', 'Diego', 'Matheus']

lista_nomes.append('Geraldo')
lista_nomes.insert(2, 'Dudu')

dudu_count = lista_nomes.count('Dudu')
print(dudu_count)
print(len(lista_nomes))
print(lista_nomes)

lista_nomes.pop()
lista_nomes.remove('Joao')
print(lista_nomes)

print(frase.upper())
print(frase.lower())
print(frase.capitalize())

frase_separada = frase.split(',')
print(frase_separada)

frase_nova = frase + ' Como vai você?'
print(frase_nova)
