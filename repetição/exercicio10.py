"""Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles."""

print('Vou te mostrar todos os números entre os que você me dizer.')
numero = int(input('Informe o 1º número: '))
numero_dois = int(input('Informe o 2º número: '))

intervalo = range(numero, numero_dois)

print(list(intervalo))