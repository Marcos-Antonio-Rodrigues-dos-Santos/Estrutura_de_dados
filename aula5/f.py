
# Importando a biblioteca de matematica
import math

# Importando a biblioteca de aleatoriedade
import random

# Inicialmente, não temos nenhum ponto 'dentro' do circulo
pontos_no_circulo = 0

# Não sorteamos também nenhum ponto
pontos_sorteados = 0

# Sortearemos então, 10.000 pontos

for i in range(10000):
    # Incrementamos o numero de pontos sorteados
    pontos_sorteados = pontos_sorteados + 1.0

    # Sorteando dois pontos x e y
    # A função uniform sorteia numeros com casas decimais
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Calculando a distancia do ponto x, y com a origem
    # A função 'hypot' da biblioteca math calcula a distancia euclidiana
    distancia = math.hypot(x, y)

    # Verificamos, entao, se a distancia encontrada
    # é compatível com nosso criterio de aceitação (<= 1)
    if distancia <= 1:
        pontos_no_circulo = pontos_no_circulo + 1.0

# Finalmente, depois de sorteados os pontos, calculamos a razão
razao_entre_total = pontos_no_circulo / pontos_sorteados

# A estimativa de pi vai ser 4 vezes esse valor
pi_estimado = 4 * razao_entre_total

# Imprimimos a estimativa
print(pi_estimado)