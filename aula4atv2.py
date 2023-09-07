# criando calculadadora que irá fazer a idade dos cachorros - cada ano do humano corresponde a 7 do cachorro # 

print("Tuco tem 2 anos, porte médio")
print("Kyhara tem 3 anos, porte médio")
print("Mel tem 5 anos, porte grande")
print("Mike tem 8 anos, porte médio")

# declarando variaveis #

cachorro_1 = "Tuco" 
cachorro_2 = "Kyhara"
cachorro_3 = "Mel"
cachorro_4 = "Mike"

idade_1 = 2
idade_2 = 3
idade_3 = 5
idade_4 = 8
idade_real = 7

porte_1 = "pequeno"
porte_2 = "médio"
porte_3  = "grande"

valor_1 = 75
valor_2 = 60
valor_3 = 50

custo_1 = 20 
custo_2 = 15 
custo_3 = 5 

quantidade_de_banho = 10

# realiza multiplicação #
resultado = idade_1 * idade_real
lucro_final = (valor_1 * quantidade_de_banho) - (custo_1 * quantidade_de_banho)

# RESULTADO FINAL #

print(f"Olá, {cachorro_1} tem {idade_real}, seu porte é {porte_2} e nos últimos 12 meses o lucro com este animal foi de {lucro_final} reais ")
