#107, 108, 109, 110, 111
import moeda
#programa principal
valor = float(input("Digite um valor R$: "))
moeda.resumo(valor, 10, 13)

#exercicios anteriores/ 107, 108 e 109
'''''
print(f"O dobro de {moeda.raio_moedizador(valor)} e {moeda.dobro(valor,True)}")
print(f"A metade de {moeda.raio_moedizador(valor)} e {moeda.metade(valor,True)}")
print(f"O valor aumentado em 10% e {moeda.aumentar(valor, 10, True)}")
print(f"O valor reduzido em 15% e {moeda.diminuir(valor, 13, True)}")
'''''