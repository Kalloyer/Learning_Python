# Tabela dos 20 priemiros times do Brasileirão, mostre os 5 primeiros colocado, os 4 ultimos colocados, uma lista em ordem alfabética, em que posição está o time Botafogo
contagem = 0
time = (
    "Atletico-PR",
    "Cruzeiro",
    "Flamengo",
    "Fortaleza",
    "Vasco da Gama",
    "Internacional",
    "Palmeiras",
    "Bragantino",
    "Fluminense",
    "Juventude",
    "Criciúma",
    "Corínthians",
    "Atlético-MG",
    "Botafogo",
    "Grêmio",
    "São Paulo",
    "Bahia",
    "Atlético-GO",
    "EC Vitória",
    "Cuiabá",
)
print(f"Lista de time do Brasileirão: {time}")
print(30 * "=====")
print(f"Os 5 primeiros colocados são: {time[:5]}")
print(30 * "=====")
print(f"Os últimos 4 colocados são: {time[-4:]}")
print(30 * "=====")
print(f"Times em ordem alfabética: {sorted(time)}")
print(30 * "=====")
for posicao in time:
    contagem += 1
    if contagem == 14:
        break
print(f"O time Botafogo está na {contagem}ª posição.")
