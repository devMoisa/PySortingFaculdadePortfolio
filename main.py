from data import gerar_produtos
from sorting import bubble_sort, quick_sort, merge_sort, heap_sort
from analysis import exibir_resultados

def main():
    print("Gerando produtos :D")
    produtos = gerar_produtos(1000)

    print("\n Ordenando produtos por preço usando diferentes algoritmos de ordenação como solicitado no portifolio")
    for algoritmo in [bubble_sort, quick_sort, merge_sort, heap_sort]:
        exibir_resultados(algoritmo, produtos, lambda x: x.preco)

if __name__ == "__main__":
    main()
