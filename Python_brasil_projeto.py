armazenamento = {"alexandre" : 456123789,
                "anderson":1245698456,
                "antonio":123456456,
                "carlos":91257581,
                "cesar":987458,
                "rosemary":789456125}

def total(armazenamento):
    espaco_total = sum(armazenamento.values())
    return round(espaco_total/1024/1024,2), "MB"

for i in armazenamento.keys():
    espaço = armazenamento[i]
    print(i, round(espaço/1024/1024,2), "MB")

print ("Espaço Total: ", total(armazenamento))
    

