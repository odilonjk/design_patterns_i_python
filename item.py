class Item(object):
    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

    def __str__(self):
        return 'Código: {:s} | Descrição: {:s} | Valor: R${:.2f}\n'.format(self.codigo, self.descricao, self.valor)

if __name__ == '__main__':

    item = Item(codigo='123', descricao='Lentilha', valor=2.00)

    print(item)