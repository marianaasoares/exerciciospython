from collections import Counter
piano_inicial = [1]*15

def achar_frequencia(lista_separada):
    contador_de_freq = Counter(lista_separada)
    print(contador_de_freq)
    maior_freq = max(contador_de_freq.values())
    for elemento in contador_de_freq.items():
        if elemento[1] == maior_freq:
            print(elemento)
            f = elemento[0]
    return f

def tocar(piano, acorde):
    lista_separada = piano[acorde[0]:acorde[1]+1]
    f = achar_frequencia(lista_separada)
    print("f = ", f)
    for elemento in range(acorde[0], acorde[1]+1):
        piano[elemento] = (piano[elemento] + f) % 9
    print("novo piano = ", piano)
    print("___________________________")
    return piano
acordes = ((10, 12),
            (4, 5),
            (1, 14),
            (6, 10),
            (9, 11),
            (11, 12),
            (9, 13),
            (8, 9),
            (5, 7),
            (11, 13),
            (8, 10),
            (11, 12),
            (11, 13),
            (8, 14),
            (3, 9),)
for acorde in acordes:
    print(tocar(piano_inicial, acorde))

