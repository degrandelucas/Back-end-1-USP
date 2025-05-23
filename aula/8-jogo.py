import random

numero_secreto = random.randint(1,10)
tentativas = 0

while True:
    chute = int(input('Digite um numero entre 1 e 10: '))
    tentativas += 1
    
    if chute == numero_secreto:
        print(f'Acertou o {numero_secreto} com {tentativas} tentativa(s)')
        break
    elif chute > numero_secreto:
        print('Tente um numero menor')
    else:
        print('Tente um numero maior')