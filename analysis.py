import time

# !! >>>> Função que mede o tempo <<<< !!
def medir_tempo(algoritmo, lista, key_func):
    inicio = time.time()
    algoritmo(lista, key_func)
    fim = time.time()
    return fim - inicio

# !! >>>> Função que exibe os resultados <<<< !!
def exibir_resultados(algoritmo, lista, key_func):
    produtos_copia = lista.copy()
    tempo = medir_tempo(algoritmo, produtos_copia, key_func)
    print(f"\n{algoritmo.__name__}: {tempo:.4f} segundos")
    for produto in produtos_copia:
        print(produto)
    print("-" * 50)
