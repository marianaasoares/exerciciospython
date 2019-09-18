"""With Python 2"""
"""def checa_vogal(nome, vogal):
    nome = nome.casefold()
    count = {}.fromkeys(vogal, 0)
    
    for caracter in nome:
        if caracter in count:
            count[caracter] += 1
    return count


vogal = 'aeiou'
nome = "thais viana do nascimento"
print(checa_vogal(nome,vogal))"""



def checa_vogal(nome,vogals, dict_vogals):
    for i in nome:
        if i in vogals:
            if i in dict_vogals.keys():
                dict_vogals[i] += 1
            else:
                dict_vogals[i] = 1
    return dict_vogals


dict_vogals = {}
nome = "mariana soares dos santos"
vogals = ('a','e','i','o','u')
print(checa_vogal(nome,vogals, dict_vogals))
    
