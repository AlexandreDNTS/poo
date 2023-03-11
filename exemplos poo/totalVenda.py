from functools import reduce


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def CalcularTotal(self):
        return self.quantidade * self.produto.valor


class Venda:
    def __init__(self):
        self.itens = []

    def ADDItem(self, item):
        self.itens.append(item)

    def ValorTotal(self):
        return reduce(lambda n, item: n + item.CalcularTotal(), self.itens, 0)


p1 = Produto('lápis', 1.5)
i1 = Item(p1, 2)
venda = Venda()
total = venda.ADDItem(i1)
total = venda.ValorTotal()
print(f'valor total da compra: {total:.2f}')
