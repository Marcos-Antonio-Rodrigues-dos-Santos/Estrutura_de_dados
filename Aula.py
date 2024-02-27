import requests
import nltk


def acharPartido(p):
    l = ()
    r = requests.get("https://dadosabertos.camara.leg.br/api/v2/blocos?ordem=ASC&ordenarPor=nome").json()
    for d in r["dados"]:
            l.__add__(d["nome"]) and l.append(d["id"])
    return(l)

print(acharPartido("Aécio Neves"))