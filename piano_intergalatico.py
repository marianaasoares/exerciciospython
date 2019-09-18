piano_inicial = [1,1,1,1,1]
acordes = ((1,2), (0,4), (0,2))

def tocar(piano, acorde):
    frequencia = 1
    for elemento in range(acorde[0],acorde[1]+1):
        piano[elemento] = (piano[elemento] +frequencia)%9
    return piano       

print(tocar(piano_inicial, acordes[0]))