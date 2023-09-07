
## determina valor da compra ##
valor_da_compra = float(70)

## se a compra for maior que 250 e menor que 500 ##

if valor_da_compra >= 250 and valor_da_compra < 500:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")

## se a compra for maior ou igual que 500 ##

elif valor_da_compra >= 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")

 ## se a compra for menor que 500 ##

else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")
