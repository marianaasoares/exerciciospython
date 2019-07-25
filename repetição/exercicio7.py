"""
Faça um programa que leia 5
números e informe o maior número.
"""

numeros = []
num = int(input('quantos numeros? '))

for i in range(num):
    numb = int(input('digite um numero: '))
    numeros.append(numb)
    
print('O maior número é: ', max(numeros)) 