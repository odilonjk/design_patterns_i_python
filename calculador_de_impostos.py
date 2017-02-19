from impostos import ISS, ICMS, Frete


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        # imposto agora recebe a classe e chama o metodo
        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


# se executar essa classe no terminal, vai rodar este if
# se outra classe chamar esta, não executara o if
# utilizaremos o if para realizar os testes
if __name__ == '__main__':

    from orcamento import Orcamento

    calculador = Calculador_de_impostos()

    orcamento = Orcamento(500)

    # estou passando a classe como parametro
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.realiza_calculo(orcamento, Frete())
