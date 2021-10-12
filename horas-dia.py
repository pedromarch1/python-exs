'''
Exercicio para interpretar as horas baseado em inputs simples. A partir disso, diz boa tarde, boa noite ou bom dia
'''
hora = int(input("\nQue horas são?\n"))


if(hora == 0):
    print("Agora é meia noite")
elif(hora == 1):
    print("Boa noite, agora é {hora} hora")
elif(hora >= 2 and hora <=5):
    print(f"Boa noite, agora são {hora} horas")
elif(hora >= 6 and hora <= 11):
    print(f"Bom dia, são {hora} horas")
elif(hora == 12):
    print("Agora é meio dia")
elif(hora >= 13 and hora <= 18):
    print(f"Boa tarde, agora são {hora} horas")
elif(hora >= 19 and hora <= 23):
    print(f"Boa noite, agora são {hora} horas da noite")
elif(hora < 0 or hora >= 24):
    print("Horário inválido. Insira um número entre 0 e 23")
