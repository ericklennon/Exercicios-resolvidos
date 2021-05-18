salario = float(input('Informe seu salário:'))
prestacao = float(input('Informe o valora da prestação:'))

porcentagem = (salario * 0.20) - salario
total = porcentagem * -1

print(total)


if prestacao > total:
    print('Emprestimo não concedido')

elif total > prestacao:
    print('Emprestimo concedido')

