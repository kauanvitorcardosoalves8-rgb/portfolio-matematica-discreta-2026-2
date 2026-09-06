# ============================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Atividade 2 - Divisibilidade, MDC e MMC
# ============================================================

nome = input("Nome: ")
matricula = input("Matrícula: ")
turno = input("Turno: ")

print("\n==========================================")
print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
print("==========================================")
print("Aluno:", nome)
print("Matrícula:", matricula)
print("Disciplina: Estruturas Matemáticas para Computação")
print("Turno:", turno)
print("==========================================")

numero1 = int(input("\nDigite o primeiro número inteiro positivo: "))
numero2 = int(input("Digite o segundo número inteiro positivo: "))

while numero1 <= 0 or numero2 <= 0:
    print("\nOs números precisam ser positivos.")
    numero1 = int(input("Digite o primeiro número inteiro positivo: "))
    numero2 = int(input("Digite o segundo número inteiro positivo: "))

print("\n==========================================")
print("DIVISIBILIDADE")
print("==========================================")

# Divisão normal
divisao = numero1 / numero2

# Divisão inteira (DIV)
div = numero1 // numero2

# Resto da divisão (MOD)
mod = numero1 % numero2

print("Divisão =", divisao)
print("DIV =", div)
print("MOD =", mod)

if mod == 0:
    print(numero1, "é divisível por", numero2)
else:
    print(numero1, "não é divisível por", numero2)

print("\n==========================================")
print("ALGORITMO DE EUCLIDES")
print("==========================================")

a = numero1
b = numero2

while b != 0:
    quociente = a // b
    resto = a % b

    print(a, "=", b, "x", quociente, "+", resto)

    a = b
    b = resto

mdc = a

print("\nMDC =", mdc)

print("\n==========================================")
print("MMC")
print("==========================================")

mmc = (numero1 * numero2) // mdc

print("MMC =", mmc)

print("\n==========================================")
print("RESULTADOS FINAIS")
print("==========================================")

print("Primeiro número:", numero1)
print("Segundo número:", numero2)
print("Divisão:", divisao)
print("DIV:", div)
print("MOD:", mod)
print("MDC:", mdc)
print("MMC:", mmc)

print("==========================================")