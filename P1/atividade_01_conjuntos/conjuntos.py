# ============================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 1 - Teoria dos Conjuntos
# ============================================================


DISCIPLINA = "Estruturas Matemáticas para Computação"


# ------------------------------------------------------------
# FUNÇÕES DE APOIO
# ------------------------------------------------------------

def limpar_tela():
    print("\n" * 3)


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


def mostrar_identificacao(nome, matricula, turno):
    print("=" * 60)
    print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
    print("ATIVIDADE 1 - TEORIA DOS CONJUNTOS")
    print("=" * 60)
    print("Aluno:", nome)
    print("Matrícula:", matricula)
    print("Disciplina:", DISCIPLINA)
    print("Turno:", turno)
    print("=" * 60)


def mostrar_titulo(titulo, nome, matricula, turno):
    limpar_tela()
    mostrar_identificacao(nome, matricula, turno)
    print("\n" + titulo)
    print("-" * 60)


def formatar_conjunto(conjunto):
    if len(conjunto) == 0:
        return "∅"

    elementos = sorted(conjunto)
    return "{" + ", ".join(str(elemento) for elemento in elementos) + "}"


def ler_conjunto(nome_conjunto):
    while True:
        entrada = input(
            f"Digite os elementos do conjunto {nome_conjunto}, separados por espaço: "
        ).strip()

        if entrada == "":
            print("O conjunto não pode ficar vazio.")
            continue

        try:
            valores = entrada.split()
            conjunto = set()

            for valor in valores:
                conjunto.add(int(valor))

            if len(conjunto) < len(valores):
                print("Elementos repetidos foram considerados apenas uma vez.")

            return conjunto

        except ValueError:
            print("Digite apenas números inteiros.")


# ------------------------------------------------------------
# OPERAÇÕES COM CONJUNTOS
# ------------------------------------------------------------

def calcular_uniao(conjunto_a, conjunto_b):
    resultado = set()

    for elemento in conjunto_a:
        resultado.add(elemento)

    for elemento in conjunto_b:
        resultado.add(elemento)

    return resultado


def calcular_intersecao(conjunto_a, conjunto_b):
    resultado = set()

    for elemento in conjunto_a:
        if elemento in conjunto_b:
            resultado.add(elemento)

    return resultado


def calcular_diferenca(conjunto_a, conjunto_b):
    resultado = set()

    for elemento in conjunto_a:
        if elemento not in conjunto_b:
            resultado.add(elemento)

    return resultado


def verificar_subconjunto(conjunto_a, conjunto_b):
    for elemento in conjunto_a:
        if elemento not in conjunto_b:
            return False

    return True


# ------------------------------------------------------------
# CONJUNTO DAS PARTES
# ------------------------------------------------------------

def conjunto_das_partes(conjunto):
    partes = [set()]

    for elemento in sorted(conjunto):
        novas_partes = []

        for parte in partes:
            nova_parte = parte.copy()
            nova_parte.add(elemento)
            novas_partes.append(nova_parte)

        for nova_parte in novas_partes:
            partes.append(nova_parte)

    return partes


def ordenar_partes(partes):
    resultado = []

    for parte in partes:
        resultado.append(parte)

    resultado.sort(key=lambda x: (len(x), sorted(x)))

    return resultado


# ------------------------------------------------------------
# PRODUTO CARTESIANO
# ------------------------------------------------------------

def calcular_produto_cartesiano(conjunto_a, conjunto_b):
    resultado = []

    for elemento_a in sorted(conjunto_a):
        for elemento_b in sorted(conjunto_b):
            resultado.append((elemento_a, elemento_b))

    return resultado


def formatar_produto_cartesiano(produto):
    if len(produto) == 0:
        return "∅"

    elementos = []

    for par in produto:
        elementos.append(f"({par[0]}, {par[1]})")

    return "{" + ", ".join(elementos) + "}"


# ------------------------------------------------------------
# PARTIÇÃO
# ------------------------------------------------------------

def criar_particao(conjunto):
    particao = []

    for elemento in sorted(conjunto):
        parte = {elemento}
        particao.append(parte)

    return particao


def verificar_particao(particao, conjunto):
    uniao = set()

    for parte in particao:
        for elemento in parte:
            if elemento in uniao:
                return False

            uniao.add(elemento)

    return uniao == conjunto


# ------------------------------------------------------------
# OPÇÃO 1 - UNIÃO
# ------------------------------------------------------------

def mostrar_uniao(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("1 - UNIÃO DOS CONJUNTOS", nome, matricula, turno)

    resultado = calcular_uniao(conjunto_a, conjunto_b)

    print("A =", formatar_conjunto(conjunto_a))
    print("B =", formatar_conjunto(conjunto_b))

    print("\nUnião:")
    print("A ∪ B =", formatar_conjunto(resultado))

    print("\nA união reúne todos os elementos de A e B")
    print("sem repetir os elementos que aparecem nos dois conjuntos.")


# ------------------------------------------------------------
# OPÇÃO 2 - INTERSEÇÃO
# ------------------------------------------------------------

def mostrar_intersecao(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("2 - INTERSEÇÃO DOS CONJUNTOS", nome, matricula, turno)

    resultado = calcular_intersecao(conjunto_a, conjunto_b)

    print("A =", formatar_conjunto(conjunto_a))
    print("B =", formatar_conjunto(conjunto_b))

    print("\nInterseção:")
    print("A ∩ B =", formatar_conjunto(resultado))

    print("\nA interseção contém somente os elementos")
    print("que pertencem simultaneamente a A e B.")


# ------------------------------------------------------------
# OPÇÃO 3 - DIFERENÇA
# ------------------------------------------------------------

def mostrar_diferenca(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("3 - DIFERENÇA DOS CONJUNTOS", nome, matricula, turno)

    resultado_ab = calcular_diferenca(conjunto_a, conjunto_b)
    resultado_ba = calcular_diferenca(conjunto_b, conjunto_a)

    print("A =", formatar_conjunto(conjunto_a))
    print("B =", formatar_conjunto(conjunto_b))

    print("\nA - B =", formatar_conjunto(resultado_ab))
    print("Elementos que pertencem a A, mas não pertencem a B.")

    print("\nB - A =", formatar_conjunto(resultado_ba))
    print("Elementos que pertencem a B, mas não pertencem a A.")


# ------------------------------------------------------------
# OPÇÃO 4 - CARDINALIDADES
# ------------------------------------------------------------

def mostrar_cardinalidades(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("4 - CARDINALIDADES", nome, matricula, turno)

    uniao = calcular_uniao(conjunto_a, conjunto_b)
    intersecao = calcular_intersecao(conjunto_a, conjunto_b)

    cardinalidade_a = len(conjunto_a)
    cardinalidade_b = len(conjunto_b)
    cardinalidade_uniao = len(uniao)
    cardinalidade_intersecao = len(intersecao)

    print("A =", formatar_conjunto(conjunto_a))
    print("B =", formatar_conjunto(conjunto_b))

    print("\nCardinalidades:")
    print("|A| =", cardinalidade_a)
    print("|B| =", cardinalidade_b)
    print("|A ∪ B| =", cardinalidade_uniao)
    print("|A ∩ B| =", cardinalidade_intersecao)

    print("\nVerificação da fórmula:")
    print("|A ∪ B| = |A| + |B| - |A ∩ B|")

    calculo = cardinalidade_a + cardinalidade_b - cardinalidade_intersecao

    print(
        f"|A ∪ B| = {cardinalidade_a} + "
        f"{cardinalidade_b} - {cardinalidade_intersecao}"
    )

    print(f"|A ∪ B| = {calculo}")


# ------------------------------------------------------------
# OPÇÃO 5 - CONJUNTO DAS PARTES
# ------------------------------------------------------------

def mostrar_conjunto_das_partes(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("5 - CONJUNTO DAS PARTES", nome, matricula, turno)

    print("Escolha o conjunto:")
    print("1 - Conjunto A")
    print("2 - Conjunto B")

    escolha = input("\nEscolha: ")

    if escolha == "1":
        conjunto = conjunto_a
        nome_conjunto = "A"

    elif escolha == "2":
        conjunto = conjunto_b
        nome_conjunto = "B"

    else:
        print("\nOpção inválida.")
        return

    partes = conjunto_das_partes(conjunto)
    partes = ordenar_partes(partes)

    print(f"\nConjunto {nome_conjunto} =", formatar_conjunto(conjunto))

    print(f"\nP({nome_conjunto}) = conjunto das partes:")

    for i, parte in enumerate(partes, start=1):
        print(f"{i:>3} - {formatar_conjunto(parte)}")

    print(f"\nQuantidade de subconjuntos: {len(partes)}")

    esperado = 2 ** len(conjunto)

    print(f"Fórmula: 2^{len(conjunto)} = {esperado}")

    if len(partes) == esperado:
        print("A quantidade está correta.")


# ------------------------------------------------------------
# OPÇÃO 6 - PARTIÇÃO
# ------------------------------------------------------------

def mostrar_particao(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("6 - EXEMPLO DE PARTIÇÃO", nome, matricula, turno)

    print("Escolha o conjunto:")
    print("1 - Conjunto A")
    print("2 - Conjunto B")

    escolha = input("\nEscolha: ")

    if escolha == "1":
        conjunto = conjunto_a
        nome_conjunto = "A"

    elif escolha == "2":
        conjunto = conjunto_b
        nome_conjunto = "B"

    else:
        print("\nOpção inválida.")
        return

    particao = criar_particao(conjunto)

    print(f"\nConjunto {nome_conjunto} =", formatar_conjunto(conjunto))

    print("\nUma partição possível é:")

    for parte in particao:
        print(formatar_conjunto(parte))

    print("\nCada elemento fica em uma única parte.")

    if verificar_particao(particao, conjunto):
        print("\nA partição é válida.")


# ------------------------------------------------------------
# OPÇÃO 7 - PRODUTO CARTESIANO
# ------------------------------------------------------------

def mostrar_produto_cartesiano(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("7 - PRODUTO CARTESIANO", nome, matricula, turno)

    produto = calcular_produto_cartesiano(conjunto_a, conjunto_b)

    print("A =", formatar_conjunto(conjunto_a))
    print("B =", formatar_conjunto(conjunto_b))

    print("\nA × B =")
    print(formatar_produto_cartesiano(produto))

    print("\nQuantidade de pares ordenados:", len(produto))

    print(
        f"\n|A × B| = |A| × |B| = "
        f"{len(conjunto_a)} × {len(conjunto_b)} = {len(produto)}"
    )


# ------------------------------------------------------------
# OPÇÃO 8 - INCLUSÃO
# ------------------------------------------------------------

def mostrar_inclusao(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("8 - RELAÇÃO DE INCLUSÃO", nome, matricula, turno)

    a_esta_em_b = verificar_subconjunto(conjunto_a, conjunto_b)
    b_esta_em_a = verificar_subconjunto(conjunto_b, conjunto_a)

    print("A =", formatar_conjunto(conjunto_a))
    print("B =", formatar_conjunto(conjunto_b))

    print("\nVerificações:")

    if a_esta_em_b:
        print("A ⊆ B : verdadeiro")
    else:
        print("A ⊆ B : falso")

    if b_esta_em_a:
        print("B ⊆ A : verdadeiro")
    else:
        print("B ⊆ A : falso")

    if a_esta_em_b and b_esta_em_a:
        print("\nOs conjuntos A e B são iguais.")

    elif a_esta_em_b:
        print("\nA está contido em B.")

    elif b_esta_em_a:
        print("\nB está contido em A.")

    else:
        print("\nNenhum dos conjuntos está contido no outro.")


# ------------------------------------------------------------
# OPÇÃO 9 - MOSTRAR TUDO
# ------------------------------------------------------------

def mostrar_tudo(conjunto_a, conjunto_b, nome, matricula, turno):
    mostrar_titulo("9 - RESUMO COMPLETO", nome, matricula, turno)

    uniao = calcular_uniao(conjunto_a, conjunto_b)
    intersecao = calcular_intersecao(conjunto_a, conjunto_b)
    diferenca_ab = calcular_diferenca(conjunto_a, conjunto_b)
    diferenca_ba = calcular_diferenca(conjunto_b, conjunto_a)
    produto = calcular_produto_cartesiano(conjunto_a, conjunto_b)

    print("A =", formatar_conjunto(conjunto_a))
    print("B =", formatar_conjunto(conjunto_b))

    print("\n--- UNIÃO ---")
    print("A ∪ B =", formatar_conjunto(uniao))

    print("\n--- INTERSEÇÃO ---")
    print("A ∩ B =", formatar_conjunto(intersecao))

    print("\n--- DIFERENÇAS ---")
    print("A - B =", formatar_conjunto(diferenca_ab))
    print("B - A =", formatar_conjunto(diferenca_ba))

    print("\n--- CARDINALIDADES ---")
    print("|A| =", len(conjunto_a))
    print("|B| =", len(conjunto_b))
    print("|A ∪ B| =", len(uniao))
    print("|A ∩ B| =", len(intersecao))

    print("\n--- CONJUNTO DAS PARTES ---")
    partes_a = conjunto_das_partes(conjunto_a)
    partes_b = conjunto_das_partes(conjunto_b)

    print("|P(A)| =", len(partes_a))
    print("|P(B)| =", len(partes_b))

    print("\n--- PRODUTO CARTESIANO ---")
    print("A × B =", formatar_produto_cartesiano(produto))

    print("\n--- INCLUSÃO ---")

    if verificar_subconjunto(conjunto_a, conjunto_b):
        print("A ⊆ B : verdadeiro")
    else:
        print("A ⊆ B : falso")

    if verificar_subconjunto(conjunto_b, conjunto_a):
        print("B ⊆ A : verdadeiro")
    else:
        print("B ⊆ A : falso")

    print("\n--- PARTIÇÃO ---")
    particao = criar_particao(conjunto_a)

    print("Exemplo de partição de A:")

    for parte in particao:
        print(formatar_conjunto(parte))


# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------

def mostrar_menu():
    print("\n" + "=" * 60)
    print("MENU - TEORIA DOS CONJUNTOS")
    print("=" * 60)

    print("1 - União")
    print("2 - Interseção")
    print("3 - Diferenças")
    print("4 - Cardinalidades")
    print("5 - Conjunto das partes")
    print("6 - Partição")
    print("7 - Produto cartesiano")
    print("8 - Relação de inclusão")
    print("9 - Mostrar tudo")
    print("0 - Sair")

    print("=" * 60)


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

def main():

    limpar_tela()

    print("=" * 60)
    print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
    print("ATIVIDADE 1 - TEORIA DOS CONJUNTOS")
    print("=" * 60)

    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    turno = input("Turno: ")

    print("\nAgora vamos criar os conjuntos.")

    conjunto_a = ler_conjunto("A")
    conjunto_b = ler_conjunto("B")

    while True:

        limpar_tela()

        mostrar_identificacao(nome, matricula, turno)

        print("\nConjuntos cadastrados:")
        print("A =", formatar_conjunto(conjunto_a))
        print("B =", formatar_conjunto(conjunto_b))

        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_uniao(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "2":
            mostrar_intersecao(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "3":
            mostrar_diferenca(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "4":
            mostrar_cardinalidades(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "5":
            mostrar_conjunto_das_partes(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "6":
            mostrar_particao(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "7":
            mostrar_produto_cartesiano(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "8":
            mostrar_inclusao(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "9":
            mostrar_tudo(
                conjunto_a,
                conjunto_b,
                nome,
                matricula,
                turno
            )
            pausar()

        elif opcao == "0":
            limpar_tela()
            mostrar_identificacao(nome, matricula, turno)
            print("\nPrograma encerrado.")
            print("Até a próxima!")
            break

        else:
            print("\nOpção inválida.")
            pausar()


# ------------------------------------------------------------
# EXECUÇÃO
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
    
