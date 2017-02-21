from impostos import ISS, ICMS, Frete


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        # imposto agora recebe a classe e chama o metodo
        imposto_calculado = imposto.calcula(orcamento)

        return imposto_calculado


# se executar essa classe no terminal, vai rodar este if
# se outra classe chamar esta, não executara o if
# utilizaremos o if para realizar os testes
if __name__ == '__main__':

    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Notebook Dell', 2600))
    orcamento.adiciona_item(Item('Monitor Dell', 900))
    orcamento.adiciona_item(Item('Teclado Genérico', 60))
    orcamento.adiciona_item(Item('Mouse Genérico', 20))

    # estou passando a classe como parametro
    iss = calculador.realiza_calculo(orcamento, ISS())
    icms = calculador.realiza_calculo(orcamento, ICMS())
    frete = calculador.realiza_calculo(orcamento, Frete())
    print('Valor ISS: R$%s' % calculador.realiza_calculo(orcamento, ISS()))
    print('Valor ISS: R$%s' % calculador.realiza_calculo(orcamento, ICMS()))
    print('Valor ISS: R$%s' % calculador.realiza_calculo(orcamento, Frete()))
