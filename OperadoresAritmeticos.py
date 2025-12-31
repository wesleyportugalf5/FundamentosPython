nome, idade, sobrenome = "João", 24, "Silva"

nome2 = input("Digite o seu nome: ")
idade2 = int(input("Digite sua idade: "))
sobrenome2 = input("Digite seu sobrenome: ")

print(type(idade2))

print(f"Olá, {nome2} {sobrenome2}, sua idade é {idade2}")

soma_idades = idade + idade2
print(f"A soma das idades é: {soma_idades}")

subtracao_idades = idade - idade2
print(f"A subtração das idades é: {subtracao_idades}")

multiplicacao_idades = idade * idade2
print(f"A multiplicação das idades é: {multiplicacao_idades}")

media_idades = (idade + idade2) / 2
print(f"A média das idades é: {media_idades}")