preco = float(input('Preço atual do produto: R$'))
precoDescont = preco * (5 / 100)
print('Preço com desconto de 5% é R${:.2f}'.format(preco - precoDescont))
