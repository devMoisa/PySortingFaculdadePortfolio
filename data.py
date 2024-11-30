import random
import datetime
from models import Produto

# !! >>>> Esta função GERA OS PRODUTOS <<<< !!
def gerar_produtos(n):
    produtos = []
    for i in range(n):
        nome = f"Produto{i}"
        preco = round(random.uniform(10, 100), 2)
        avaliacao = round(random.uniform(0, 5), 2)
        data_adicao = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
        categoria = f"Categoria{random.randint(1, 5)}"
        produtos.append(Produto(nome, preco, avaliacao, data_adicao, categoria))
    return produtos
