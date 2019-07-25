def validar_populacao(pop):
    if pop < 0:
        print("Valor inválido")
    return pop < 0

popA = int(input("População do país A: "))

while(validar_populacao(popA) == True):
    popA = int(input("População do país A: "))
    
popB = int(input("População do país B: "))
while(validar_populacao(popB) == True):
    popB = int(input("População do país B: "))
    
variacaoA = float(input("taxas de crescimento do país A:"))
variacaoB = float(input("taxas de crescimento do país B:"))
anos = 0

def taxa_de_crescimento(variacao):
    return (variacao/100) + 1

while (popA < popB):
    popA = popA * taxa_de_crescimento(variacaoA)
    popB = popB * taxa_de_crescimento(variacaoB)
    anos = anos + 1
    
print(anos)
