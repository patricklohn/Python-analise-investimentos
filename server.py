investimentos = [
    {"nome": "Empresa X", "custo": 30000, "retorno": 40000},
    {"nome": "Empresa Y", "custo": 50000, "retorno": 60000},
    {"nome": "Imóvel Z", "custo": 40000, "retorno": 45000},
    {"nome": "Títulos públicos", "custo": 10000, "retorno": 15000},
    {"nome": "Fundo de investimento F", "custo": 20000, "retorno": 25000},
]

orcamento = 100000

def bestInvestiment(investimentos, orcamento):
    n = len(investimentos)
    melhor_percentual = 0
    melhor_comb = []

    for i in range(1, 2**n):
        combinacao_atual = []
        custo_total = 0
        retorno_total = 0

        for j in range(n):
            if (i >> j) & 1:
                combinacao_atual.append(investimentos[j]["nome"])
                custo_total += investimentos[j]["custo"]
                retorno_total += investimentos[j]["retorno"]

        if custo_total <= orcamento:
            percentual_retorno = (retorno_total - custo_total) / custo_total
            if percentual_retorno > melhor_percentual:
                melhor_percentual = percentual_retorno
                melhor_comb = combinacao_atual

    return melhor_comb, melhor_percentual

melhor_comb, melhor_percentual = bestInvestiment(investimentos, orcamento)
print(f"A melhor combinação de investimentos é: {melhor_comb}")
print(f"O percentual de retorno é: {melhor_percentual * 100:.2f}%")
