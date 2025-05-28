import random
import pandas as pd

def gerar_cartela():
    faixas = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    faixas['N'][2] = 'Free'  # Centro livre
    return pd.DataFrame(faixas)

def gerar_varias_cartelas(qtd):
    cartelas = []
    for i in range(qtd):
        cartelas.append(gerar_cartela())
    return cartelas

# Gerar 1000 cartelas
cartelas = gerar_varias_cartelas(10)

# Exibir a primeira cartela como exemplo
def exibir_cartela(cartela):
    for cartelas in cartela:
        print(cartelas)
        print("\n")

exibir_cartela(cartelas)
