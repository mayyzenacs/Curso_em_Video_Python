#funções

def aumentar(value=0, aumentu=0,show=True):
    au = value + (value * aumentu / 100)
    if show:
        return raio_moedizador(au)
    return au

def diminuir(value, diminui,show=True):
    di = value - (value * diminui / 100)
    if show:
        return raio_moedizador(di)
    return di

def dobro(value,show=True):
    do = value * 2
    if show:
        return raio_moedizador(do)
    return do

def metade(value,show=True):
    me = value / 2
    if show:
        return raio_moedizador(me)
    return me

def raio_moedizador(value,moeda="R$"):
    return f"{moeda}{value:.2f}".replace(".",",")

def resumo(value, aumento, diminui):
    print('-'*30)
    print(f"Preco analisado:{raio_moedizador(value):>12}")
    print(f"Dobro do preco:{dobro(value):>12}")
    print(f"Metade do preco:{metade(value):>12}")
    print(f"{aumento} de aumento:{aumentar(value, aumento):>12}")
    print(f"{diminui} de reducao:{diminuir(value,diminui):>12}")
