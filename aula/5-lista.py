numeros = [1,2,3,4,5]

print(numeros)
print("primeiro elemento da lista:", numeros[0]) # saida: 1
print('último elemento da lista:', numeros[4]) # saida: 5
print('último elemento da lista:', numeros[-1]) # saida: 5

numeros.append(6)

print(numeros)

print('último elemento da lista:', numeros[-1]) # saida: 6

numeros.remove(3)

print(numeros)

print("exibindo os elementos da lista: ")

for numero in numeros:
    print(numero)

print("Verificando se um elemento está na lista")

carros = ['Ferrari', 'Land Rover', 'Mustang', 'Fusca']

carro_procurado = 'Fusca'

if carro_procurado in carros:
    print('O Fusca está presente na lista')
else:
    print('O carro nao está presente')


