cidades = ('Salvador',"Maceio","Natal","São Paulo","Floripa","Guarapari")
print (f'A tupla de cidades: {cidades}')
cidades_lista = list (cidades)
print(type(cidades_lista))
print ('-'*30)

cidades_lista.append("Manaus")
cidades_lista.append("Belo Horizonte")
print(f'A lista com duas cidades adicionadas: {cidades_lista}')
print('-'*30)

cidades_lista.remove("Salvador")
print(f'A lista sem o primeiro item {cidades_lista}')
print ('-'*30)

cidades_lista.pop()
print(f'A lista sem o último item {cidades_lista}')
print(f'A primeira cidade é: {cidades_lista[0]}')
print(len(cidades_lista))
print ('-'*30)

pessoa = {"nome": "Giovanna", "idade": 21, "profissão": "analista de mis"}
print(pessoa["nome"])