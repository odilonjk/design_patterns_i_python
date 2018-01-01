from abc import ABCMeta, abstractmethod

# Classe abstrata para calculo genérico de máxima
# ou mínima taxação do imposto.
class TemplateImpostoCondicional(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    # Esta anotação exige que o método seja implementado
    # na classe filha.
    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ISS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class Frete(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.02

# Utilizando classe abstrata.
class ICPP(TemplateImpostoCondicional):

    # Implementado os métodos exigidos.
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500
            
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(TemplateImpostoCondicional):

    def __tem_item_mais_caro_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_mais_caro_que_100_reais
            
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    