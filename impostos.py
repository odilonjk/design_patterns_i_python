from abc import ABCMeta, abstractmethod

class Imposto(object):

    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    def calcula_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass


# Classe abstrata para calculo genérico de máxima
# ou mínima taxação do imposto.
class TemplateImpostoCondicional(Imposto):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calcula_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calcula_outro_imposto(orcamento)

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


def IPVX(metodo):
    def wrapper(self, orcamento):
        return metodo(self, orcamento) + 50.0
    return wrapper


class ISS(Imposto):

    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calcula_outro_imposto(orcamento)


class ICMS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calcula_outro_imposto(orcamento)


class Frete(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.02 + self.calcula_outro_imposto(orcamento)

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
