def checa_vogal(nome, vogal):
    nome = nome.casefold()
    count = {}.fromkeys(vogal, 0)
    
    for caracter in nome:
        if caracter in count:
            count[caracter] += 1
    return count


vogal = 'aeiou'
nome = "thais viana do nascimento"
print(checa_vogal(nome,vogal))
