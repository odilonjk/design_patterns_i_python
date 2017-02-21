# -*- coding: UTF-8 -*-
from descontos import Desconto_por_valor, Desconto_por_cinco_itens


class Calculador_de_descontos(object):
    """Retorna valor de desconto baseado no orçamento"""

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens().calcula(orcamento)
        if(desconto == 0):
            desconto = Desconto_por_valor().calcula(orcamento)
        return desconto


if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Notebook Dell', 2600))
    orcamento.adiciona_item(Item('Monitor Dell', 900))
    orcamento.adiciona_item(Item('Teclado Genérico', 60))
    orcamento.adiciona_item(Item('Mouse Genérico', 20))

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)

    print('Valor de desconto: R$%s ' % desconto)
