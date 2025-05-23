produtos = []

while True:
    nome = input('Nome do produto: ')
    categoria = input('Nome da categoria: ')
    preco = float(input('Preco do produto: '))
    
    produtos.append({
        'nome': nome,
        'categoria': categoria,
        'preco': preco
    }
    )
    
    continuar = input('Deseja cadastrar outro produto? (s/n) ')
    if continuar.lower() != 's':
        break
    
print('Produtos cadastrados: ')
for produto in produtos:
    print(f'nome: {produto['nome']} | categoria: {produto['categoria']} | preco: {produto['preco']}')