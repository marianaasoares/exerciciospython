class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def chamar_ponto(self):
        print("x: ",self.x,"y: ", self.y)
        return None
    
    def testa_pertencimento(self, retangulo):
        if retangulo.vertice_partida.x < self.x < retangulo.largura + retangulo.vertice_partida.x and retangulo.vertice_partida.y < self.y < retangulo.altura +retangulo.vertice_partida.y:
            return True
        return False
    
    def __str__(self):
        return "({} , {})".format(self.x, self.y)
    
class Retangulo:
    def __init__(self, altura, largura, vertice_partida):
        self.altura = altura
        self.largura = largura
        self.vertice_partida = vertice_partida
    
    def encontrar_centro(self):
        x = self.vertice_partida.x + self.altura/2
        y= self.vertice_partida.y + self.largura/2
        return Ponto(x,y)
    
p1 = Ponto(10,15)
p2 = Ponto(0.4,0.6)
#print(ponto)
#ponto.chamar_ponto()
retangulo1 = Retangulo(1,1, Ponto(0,0))
#print(retangulo1.encontrar_centro())

retangulo2 = Retangulo(1,1, Ponto(0,0))
#print(retangulo2.encontrar_centro())

retangulo3 = Retangulo(1,1, Ponto(0,0))
#print(retangulo3.encontrar_centro())


retangulo4 = Retangulo(1,1, Ponto(0,0))

#print(retangulo4.encontrar_centro())

print(p1.testa_pertencimento(retangulo4))
print(p2.testa_pertencimento(retangulo4))