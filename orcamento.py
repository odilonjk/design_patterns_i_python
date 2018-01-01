# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class EstadoOrcamento(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass
    
    @abstractmethod
    def finaliza(self, orcamento):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Em_Aprovacao(EstadoOrcamento):
    def __str__(self):
        return 'Em aprovação.'
    
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()
    
    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Um orçamento em aprovação não pode ser finalizado.')

class Aprovado(EstadoOrcamento):
    def __str__(self):
        return 'Aprovado.'

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception('O orçamento já esta aprovado.')
    
    def reprova(self, orcamento):
        raise Exception('Um orçamento aprovado não pode ser reprovado.')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(EstadoOrcamento):
    def __str__(self):
        return 'Reprovado.'

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Não é possível dar desconto extra em orçamentos reprovados.')

    def aprova(self, orcamento):
        raise Exception('Um orçamento reprovado não pode ser aprovado.')
    
    def reprova(self, orcamento):
        raise Exception('O orçamento já esta reprovado.')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(EstadoOrcamento):
    def __str__(self):
        return 'Finalizado.'

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Não é possível dar desconto extra em orçamentos finalizados.')
    
    def aprova(self, orcamento):
        raise Exception('Um orçamento finalizado não pode ser aprovado.')
    
    def reprova(self, orcamento):
        raise Exception('Um orçamento finalizado não pode ser reprovado.')

    def finaliza(self, orcamento):
        raise Exception('O orçamento já esta finalizado.')

class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_Aprovacao()
        self.__desconto_extra = 0

    # quando a propriedade for acessada, ela soma o valor de todos itens.
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aplica_desconto_extra(self):
        if self.__desconto_extra > 0:
            raise Exception('Este orçamento já recebeu desconto extra.')
        else:
            self.estado_atual.aplica_desconto_extra(self)
            self.__recebeu_desconto_extra = True

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

# um item criado não pode ser alterado, suas propriedade são apenas de leitura
class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

if __name__ == '__main__':
    from calculador_de_descontos import Calculador_de_descontos

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Notebook Dell', 2600))
    orcamento.adiciona_item(Item('Monitor Dell', 900))
    orcamento.adiciona_item(Item('Teclado Genérico', 60))
    orcamento.adiciona_item(Item('Mouse Genérico', 20))

    # calculador_de_descontos = Calculador_de_descontos()
    # desconto = calculador_de_descontos.calcula(orcamento)

    # print('Valor de desconto: R$%s ' % desconto)
    print('Valor do orçamento %s' % orcamento.valor)
    orcamento.aplica_desconto_extra()
    print(orcamento.estado_atual)
    print('Valor do orçamento %s' % orcamento.valor)
    orcamento.aprova()
    
    # orcamento.aplica_desconto_extra()
    print(orcamento.estado_atual)
    print('Valor do orçamento %s' % orcamento.valor)
    orcamento.finaliza()
    print(orcamento.estado_atual)