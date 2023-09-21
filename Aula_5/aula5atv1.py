# idade = int(input("Digite sua idade"))
idade = 18

if idade >= 18: 
    print("Indivíduo possui idade mínima para dirigir e para ser preso")

elif idade >= 16 and idade <= 17: 
    print("Indivíduo tem entre 16 e 17 anos e ainda NÃO está apto para dirigir e nem ser preso")

else:
    print("Indivíduo NÃO possui idade mínima para dirigir")