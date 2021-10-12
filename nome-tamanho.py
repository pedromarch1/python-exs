'''
Exercicio para descobrir o tamanho de nome do usuario usando strings e len() para calcular o tamanho
'''
nome = str(input("\nOlá.\nPor favor, digite seu nome:\n"))

if(len(nome) <= 5):
    print(f"Nome curto, ein {nome}?")
elif(len(nome) > 6 and len(nome) <= 8):
    print(f"Nome na média, {nome}")
else:
    print(f"Que nome longo o seu, {nome}!")