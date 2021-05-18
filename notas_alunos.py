ficha = []

while True:

    nota1 = int(input("Insira a nota 1: "))
    while nota1 < 0 or nota1 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota1 = float(input("Insira a nota 1: "))

    nota2 = int(input("Insira a nota 2: "))
    while nota2 < 0 or nota2 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota2 = int(input("Insira a nota 2: "))

    media = (nota1 + nota2) / 3
    print(media)
    ficha.append([[nota1, nota2], media])

    resposta = str(input("Quer continuar? [S/N]"))
    if resposta in 'Nn':
        break
