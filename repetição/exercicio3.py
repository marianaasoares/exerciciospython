def validar_idade(idade):
    return 0 < idade < 150

def validar_sexo(sexo):
    return sexo == 'm' or sexo == 'f'

def validar_nome(nome):
    return len(nome) > 3

def validar_salario(salario)
    return salario > 0

def validar_estado_civil(estado_civil):
    return estado_civil in ['s', 'c', 'v', 'd']

idade = input("Qual é a sua idade:")
print(validar_idade(nome))

nome = input("Qual seu nome?")
print(validar_nome(nome))

salario = input("Qual é o seu salário?")
print(validar_salario(float(salario)))

sexo = input("Qual seu sexo?")
print(validar_sexo(sexo))

estado_civil = input("Qual é o seu estado civil?")
print(validar_estado_civil(estado_civil))


