popA = 80000
popB = 200000
anos = 0

while(popA < popB):
    popA = popA * 1.03
    popB = popB * 1.015
    print(popA + popB) """irá printar a população de A e B enquanto os anos vão passando"""
    anos = anos + 1
    
print(anos)    
