def calcula_ISS(orcamento):
    return orcamento.valor() * 0.1


def calcula_ICMS(orcamento):
    return orcamento.valor() * 0.06


def calcula_frete(orcamento):
    return orcamento.valor() * 0.02
