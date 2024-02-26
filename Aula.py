import requests

def acharPartido(p):
    c = 0
    r = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
    resp = requests.get(r).json()
    for d in resp["dados"]:
        if d["nome"] == (p):
            c += 1
    return(c)
print(acharPartido("Aécio Neves"))