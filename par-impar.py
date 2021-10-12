'''
Exercicio para descobrir se o numero digitado é par ou impar, 
baseado no principio de que um numero par pode ser dividido por 2 sem ter resto
Alem disso, determina se é inteiro ou não
'''

nmr = int(input("Olá\nPor favor, digite um numero:\n"))

if (int(nmr) == nmr):
    if(nmr % 2 == 0):
        print(f"O número {nmr} é par")
    else:
        print(f"O número {nmr} é ímpar")
else:
    print("Não inteiro")