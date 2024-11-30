
# !! >>>> Algoritmo Bubble Sort
def bubble_sort(lista, key_func):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if key_func(lista[j]) > key_func(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# !! >>>> Algoritmo Quick Sort
def quick_sort(lista, key_func):
    if len(lista) <= 1:
        return lista
    pivot = key_func(lista[0])
    menores = [x for x in lista[1:] if key_func(x) <= pivot]
    maiores = [x for x in lista[1:] if key_func(x) > pivot]
    return quick_sort(menores, key_func) + [lista[0]] + quick_sort(maiores, key_func)


# !! >>>> Algoritmo Merge Sort
def merge_sort(lista, key_func):
    if len(lista) > 1:
        mid = len(lista) // 2
        esquerda = lista[:mid]
        direita = lista[mid:]
        merge_sort(esquerda, key_func)
        merge_sort(direita, key_func)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if key_func(esquerda[i]) < key_func(direita[j]):
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1


# !! >>>> Algoritmo Heap Sort
def heap_sort(lista, key_func):
    def heapify(arr, n, i):
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n and key_func(arr[esquerda]) > key_func(arr[maior]):
            maior = esquerda

        if direita < n and key_func(arr[direita]) > key_func(arr[maior]):
            maior = direita

        if maior != i:
            arr[i], arr[maior] = arr[maior], arr[i]
            heapify(arr, n, maior)

    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
