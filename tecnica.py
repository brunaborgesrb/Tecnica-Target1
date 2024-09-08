# Programa para verificar se um número pertence à sequência de Fibonacci

def is_fibonacci(num):
    # Função auxiliar para verificar se um número é quadrado perfeito
    def is_perfect_square(x):
        s = int(x ** 0.5)
        return s * s == x

    # Um número pertence à sequência de Fibonacci se um dos dois resultados for quadrado perfeito
    def check_fibonacci(n):
        return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

    if check_fibonacci(num):
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

# Teste
numero = int(input("Informe um número: "))
print(is_fibonacci(numero))

# Programa para verificar a existência da letra ‘a’ em uma string e contar sua ocorrência

def contar_letras_a(string):
    # Contar a ocorrência de 'a' ou 'A'
    count = string.lower().count('a')
    
    if count > 0:
        return f"A letra 'a' aparece {count} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

# Teste
frase = input("Informe uma string: ")
print(contar_letras_a(frase))

# Resultado da variável SOMA ao final do processamento

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)