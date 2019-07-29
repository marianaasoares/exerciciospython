"""Altere o programa anterior para mostrar no final a soma dos números."""

print('Vou te mostrar a soma de todos os números entre os que você me dizer.')
numero = int(input('Informe o 1º número: '))
numero_dois = int(input('Informe o 2º número: '))

intervalo = list(range(numero, numero_dois))
print(sum(intervalo))

