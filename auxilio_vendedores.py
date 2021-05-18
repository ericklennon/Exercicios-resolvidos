total = float(input('Informe o valor total do produto:'))

total_a_pagar = total * 0.10
valor_desconto = total_a_pagar - total
parcela = total / 3
valor_comissao = total * 1.05



print('Valor com desconto 10%:', valor_desconto * -1)
print('Valor de cada parcela 3x: %.2f' % parcela)
print('Valor total com comissão do vendedor', valor_comissao)

