numeros = []
num = int(input('quantos numeros? '))

for i in range(num):
    numb = int(input('digite um numero: '))
    numeros.append(numb)
    
print('a soma é: ', sum(numeros), '\nE a média é ', (sum(numeros)/len(numeros)))