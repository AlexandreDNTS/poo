class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Olá, meu nome é", self.nome, "e eu tenho", self.idade, "anos.")


pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

pessoa1.apresentar()
pessoa2.apresentar()

"""
Neste exemplo, temos uma classe chamada Pessoa que tem dois atributos: nome e 
idade. A classe também tem um método apresentar que imprime uma mensagem na tela 
com o nome e a idade da pessoa.

Em seguida, criamos duas instâncias da classe Pessoa (pessoa1 e pessoa2) e chamamos o 
método apresentar para cada uma delas. Isso imprimirá na tela as informações de cada 
pessoa.
"""
