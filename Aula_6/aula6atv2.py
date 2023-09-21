# define e mostra numero da tabuada que eu quero #

numero = int("9")
print (numero)

# cria linha tracejada #
print('-'*30)

# resultado tabuada #

print(f'TABUADA DE {numero}')
print('-'*30)

for i in range (1,11): 
    valor = i * numero
    print(f'{i} X {numero} : {valor}')
