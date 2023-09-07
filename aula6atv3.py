# define frutas aleatorias # 

frutas = ['banana','uva','morango','kiwi','carambola','pera','tomate']

# define frutas alergia # 

alergias = ['banana','uva','tomate']

# resultado final # 

for fruta in frutas: 
    if fruta in alergias: 
        print(f'O que você tem alergia, {fruta} está contida na lista') 

